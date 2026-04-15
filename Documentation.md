# 📖 Documentação Técnica - FinFree AI

Esta documentação detalha a arquitetura, o fluxo de dados e as decisões de design implementadas no Agente FinFree.

---

## 🏗️ 1. Arquitetura do Sistema

O FinFree opera sob o padrão **RAG (Retrieval-Augmented Generation)** local, processando bases de dados estruturadas para alimentar o prompt do modelo de linguagem (LLM).

### Componentes Core:
* **Engine de IA:** Ollama executando o modelo `llama3.2:1b`.
* **Camada de Dados:** Pandas para ingestão e normalização de arquivos CSV e JSON.
* **Interface:** Streamlit para gerenciamento de estado da sessão e chat.
* **Gestão de Ambiente:** Poetry para isolamento de dependências e Pyenv para consistência da versão Python (3.10.12).
---
## 🔄 2. Fluxo de Processamento de Dados

Para garantir que a IA não cometa erros de cálculo, o fluxo de dados segue estas etapas:

1.  **Ingestão e Sanitização:**
    * O arquivo `transacoes.csv` é carregado via Pandas.
    * É aplicada a conversão forçada de tipos (`pd.to_numeric`) para evitar erros de soma em colunas de valor.
2.  **Enriquecimento de Contexto:**
    * Antes de enviar a pergunta ao modelo, o sistema calcula o saldo total e agrupa gastos por categoria.
    * Esses metadados são injetados no `System Prompt` como "Verdades Absolutas".
3.  **Memória Contextual:**
    * O arquivo `historico_atendimento.csv` é lido para recuperar as últimas interações, permitindo que o usuário faça perguntas como "Por que você disse aquilo antes?".
---

## 🧠 3. Engenharia de Prompt (Prompt Engineering)

O sucesso do FinFree reside na estrutura do seu **System Prompt**, que é dividido em três camadas:
* **Persona:** "Você é um mentor financeiro sênior, focado em clareza e segurança."
* **Restrições:** "Nunca sugira investimentos fora do perfil de risco do usuário. Se não houver dados de saldo, não invente números."
* **Base de Conhecimento:** Injeção direta dos DataFrames convertidos em texto legível para a IA.

---

## 🛠️ 4. Decisões de Design (Trade-offs)

### Por que Llama 3.2:1b?
Optamos por um modelo de parâmetros reduzidos (1b) para garantir que a aplicação rode em hardware doméstico com baixa latência, mantendo a privacidade total (Offline).

### Por que Poetry em vez de Pip?
O Poetry garante que a instalação seja **determinística**. O arquivo `poetry.lock` assegura que todos os desenvolvedores utilizem exatamente as mesmas versões das bibliotecas, evitando o erro "funciona na minha máquina".

---
## 🧪 5. Guia de Manutenção

### Adicionando Novos Dados
Para expandir o conhecimento do agente, basta atualizar os arquivos na pasta `/data`:
* `perfil_investidor.json`: Altere metas e apetite a risco.
* `produtos_financeiros.json`: Adicione novas opções de investimento para a IA recomendar.

### Logs de Erro
Caso o agente apresente comportamentos inesperados, verifique o console do Streamlit. Erros comuns de tipagem no CSV são tratados automaticamente, mas registros mal formatados podem ser ignorados pelo parser do Pandas.

---

## 📈 6. Roadmap de Evolução
1.  Implementação de análise preditiva (previsão de gastos para o próximo mês).
2.  Conexão direta via API com instituições bancárias (Open Banking).
3.  Suporte a múltiplos perfis de usuários no mesmo ambiente.

---
*Documentação atualizada em Abril de 2026.*
