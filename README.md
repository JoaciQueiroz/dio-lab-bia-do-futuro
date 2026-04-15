# 🤖 Agente Financeiro Inteligente com IA Generativa
# 💸 FinFree - Agente Financeiro Digital

O **FinFree** é um agente financeiro digital desenvolvido em **Python + Streamlit**, que ajuda usuários a organizar orçamento, simular investimentos e acompanhar metas financeiras de forma clara e personalizada.

---

## 📂 Estrutura do Projeto

finfree/ ├── data/ │ ├── transacoes.csv # Histórico de transações │ ├── historico_atendimento.csv # Histórico de atendimentos │ ├── perfil_investidor.json # Perfil e preferências do cliente │ ├── produtos_financeiros.json # Catálogo de produtos financeiros │ ├── metas_financeiras.json # Objetivos financeiros │ └── alertas.json # Alertas financeiros ├── src/ │ ├── chat.py # Página de chat com o agente │ ├── dashboard.py # Página de dashboards financeiros │ └── utils.py # Funções auxiliares (carregar dados) ├── app.py # Arquivo principal (multipage Streamlit) ├── prompts.md # Definição de prompts e regras do agente ├── examples.md # Dataset inicial com mocks └── README.md # Documentação do projeto

---

## ⚙️ Setup do Ambiente

### 1. Instalar Python com pyenv
```bash
pyenv install 3.11.6
pyenv local 3.11.6
2. Criar ambiente com Poetry
poetry init
poetry add streamlit langchain pandas plotly ollama
poetry shell
________________________________________
🚀 Executando o Projeto
1. Rodar o Streamlit
streamlit run src/finfree/app.py
2. Navegação
•	Chat → interação com o agente FinFree.
•	Dashboards → visualização de transações, metas, alertas e simulações.
________________________________________
📊 Funcionalidades
•	Chat → Respostas personalizadas com base em perfil, histórico e produtos.
•	Dashboards → 
o	Distribuição de gastos por categoria.
o	Regra 50-30-20 aplicada à renda mensal.
o	Comparativo de risco vs liquidez dos produtos.
o	Progresso das metas financeiras.
o	Alertas financeiros proativos.
o	Simulação de investimentos (Tesouro Selic vs Fundo ESG).
________________________________________
🧠 Prompts
O comportamento do agente é definido em prompts.md, incluindo:
•	System Prompt com regras claras.
•	Few-Shot Prompting para consistência nas respostas.
•	Tratamento de edge cases (informações sensíveis, dados incompletos).
________________________________________
📈 Diagrama de Fluxo Expandido
flowchart TD
    subgraph Base_de_Conhecimento
        A1[transacoes.csv\nHistórico de transações]
        A2[historico_atendimento.csv\nHistórico de atendimentos]
        A3[perfil_investidor.json\nPerfil e preferências]
        A4[produtos_financeiros.json\nProdutos e serviços]
        A5[metas_financeiras.json\nMetas e objetivos]
        A6[alertas.json\nAlertas financeiros]
    end

    subgraph Agente_FinFree
        B1[Carregamento de dados]
        B2[Montagem de contexto]
        B3[Motor de decisão\n(Orçamento 50-30-20,\nPerfil de risco,\nSimulações,\nMetas,\nAlertas)]
        B4[Resposta personalizada]
    end

    subgraph Dashboards
        D1[Distribuição de gastos]
        D2[Comparativo risco vs liquidez]
        D3[Progresso das metas]
        D4[Alertas financeiros]
        D5[Simulação de investimentos]
    end

    subgraph Usuario
        U1[Entrada do usuário\n(Pergunta ou solicitação)]
        U2[Saída do agente\n(Resposta clara e confiável)]
    end

    A1 --> B1
    A2 --> B1
    A3 --> B1
    A4 --> B1
    A5 --> B1
    A6 --> B1

    B1 --> B2
    B2 --> B3
    B3 --> B4

    B4 --> U2
    U1 --> B2

    B3 --> D1
    B3 --> D2
    B3 --> D3
    B3 --> D4
    B3 --> D5
________________________________________
🎯 Objetivo
O FinFree foi projetado para ser:
•	Confiável → nunca inventar dados.
•	Consistente → usar histórico e contexto.
•	Personalizado → adaptar recomendações ao perfil do usuário.
•	Seguro → tratar edge cases com responsabilidade.

---
