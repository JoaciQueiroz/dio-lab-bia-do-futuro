import pandas as pd
import json
import unidecode
import requests
from datetime import datetime

# Importação das configurações (certifique-se de que o arquivo config.py exista)
try:
    from finfree.config import OLLAMA_URL, OLLAMA_MODEL
except ImportError:
    OLLAMA_URL = "http://localhost:11434"
    OLLAMA_MODEL = "llama3.2:1b"

def carregar_dados():
    """Carrega os dados dos arquivos CSV e JSON, tratando erros de arquivos ausentes."""
    try:
        transacoes = pd.read_csv("data/transacoes.csv", encoding="utf-8")
    except Exception:
        transacoes = pd.DataFrame()

    try:
        historico = pd.read_csv("data/historico_atendimento.csv", encoding="utf-8")
    except Exception:
        historico = pd.DataFrame()

    def carregar_json(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    perfil = carregar_json("data/perfil_investidor.json")
    produtos = carregar_json("data/produtos_financeiros.json")
    metas = carregar_json("data/metas_financeiras.json")
    alertas = carregar_json("data/alertas.json")

    return transacoes, historico, perfil, produtos, metas, alertas

def montar_contexto(transacoes, historico, perfil, produtos, metas, alertas):
    # 1. Inteligência de Tempo
    data_hoje = datetime.now().strftime("%d de %B de %Y")
    
    # --- INICIALIZAÇÃO PARA SEGURANÇA ---
    saldo_total = 0
    resumo_gastos = {} # Nome padronizado
    listagem_transacoes = [] # Nome padronizado

    # 2. Cálculos Precisos
    if transacoes is not None and not transacoes.empty:
        # GARANTIA 1: Forçar a coluna 'valor' para numérico (evita erros de soma)
        transacoes['valor'] = pd.to_numeric(transacoes['valor'], errors='coerce').fillna(0)

        # GARANTIA 2: Limpar a coluna 'tipo' contra espaços, maiúsculas E acentos
        # Usamos .replace para garantir que 'saída' e 'saida' sejam lidos como a mesma coisa
        tipo_limpo = transacoes['tipo'].astype(str).str.lower().str.strip()
        tipo_limpo = tipo_limpo.str.replace('saída', 'saida', regex=False)

        # GARANTIA 3: Cálculo total sobre o DataFrame INTEIRO
        total_entradas = transacoes[tipo_limpo == 'entrada']['valor'].sum()
        total_saidas = transacoes[tipo_limpo == 'saida']['valor'].sum()
        
        # O Saldo Real
        saldo_total = total_entradas - total_saidas

        # Agrupamento para a IA ver os totais consolidados
        resumo_gastos = transacoes[tipo_limpo == 'saida'].groupby('categoria')['valor'].sum().to_dict()
        
        listagem_transacoes = transacoes.tail(20).to_dict(orient='records')
    else:
        listagem_transacoes = "Nenhum registro encontrado."

    # 3. Extração do perfil e produtos
    # Usando {} como padrão caso perfil ou produtos venham vazios/None
    perfil = perfil if perfil else {}
    produtos = produtos if produtos else {}
    
    catalogo_investimentos = produtos.get('produtos', [])
    dados_cliente = perfil.get('cliente', {})
    renda = dados_cliente.get('renda_mensal', 0)
    
    # 4. Montagem do Contexto (Agora os nomes coincidem!)
    contexto = f"""
    --- DATA ATUAL DO SISTEMA ---
    {data_hoje}

    --- PERFIL DO INVESTIDOR ---
    Nome: {dados_cliente.get('nome', 'N/A')}
    Perfil de Risco: {dados_cliente.get('perfil_risco', 'N/A')}
    Renda Mensal: R$ {renda:.2f}
    Preferências: {json.dumps(dados_cliente.get('preferencias', {}), ensure_ascii=False)}

    --- RESUMO FINANCEIRO REAL (NÃO INVENTAR VALORES) ---
    SALDO ATUAL EM CONTA: R$ {saldo_total:.2f}
    GASTOS TOTAIS POR CATEGORIA:
    {json.dumps(resumo_gastos, ensure_ascii=False, indent=2)}

    --- CATÁLOGO DE PRODUTOS FINANCEIROS DISPONÍVEIS ---
    {json.dumps(catalogo_investimentos, ensure_ascii=False, indent=2)}

    --- METAS E ALERTAS ---
    METAS: {json.dumps(metas, ensure_ascii=False)}
    ALERTAS ATIVOS: {json.dumps(alertas, ensure_ascii=False)}

    --- ÚLTIMAS 10 TRANSAÇÕES ---
    {json.dumps(listagem_transacoes, ensure_ascii=False)}
    
    INSTRUÇÃO: Use os dados acima para responder de forma precisa. 
    Se o usuário perguntar por um gasto que não está nas 'Últimas Transações', verifique a seção 'GASTOS TOTAIS POR CATEGORIA'.
    """
    return contexto

def definir_system_prompt():
    """Lê o arquivo de comportamento do agente."""
    try:
        with open("docs/system_prompt.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Você é o FinFree, um assistente financeiro. Use tabelas e seja empático."

def chamar_ollama(prompt, contexto, pergunta):
    """Faz a chamada ao modelo local com temperatura baixa para evitar alucinações."""
    # Reforço negativo para evitar que o modelo imprima títulos de instrução
    instrucao_limpeza = "\nResponda diretamente ao usuário. Não imprima títulos como 'Diagnóstico' ou 'Saudação'."
    
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f"{prompt}\n{instrucao_limpeza}\n\nCONTEXTO DE DADOS:\n{contexto}\n\nPERGUNTA DO USUÁRIO: {pergunta}\n\nFinFree:",
        "stream": False,
        "options": {
            "temperature": 0.1,  # Reduz a "criatividade" para focar nos dados reais
            "top_p": 0.1
        }
    }

    try:
        response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, timeout=30)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        return f"Erro na API: {response.status_code}"
    except Exception as e:
        return f"Erro de conexão com Ollama: {e}"

# ================= CHATBOT INTERATIVO (TERMINAL) =================
def finfree_chat():
    """Função para testar o agente via terminal."""
    transacoes, historico, perfil, produtos, metas, alertas = carregar_dados()
    contexto = montar_contexto(transacoes, historico, perfil, produtos, metas, alertas)
    system_prompt = definir_system_prompt()

    print("👋 Olá! Eu sou o FinFree. (Digite 'sair' para encerrar)")
    
    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break

        resposta = chamar_ollama(system_prompt, contexto, pergunta)
        print(f"\nFinFree: {resposta}")

if __name__ == "__main__":
    finfree_chat()
