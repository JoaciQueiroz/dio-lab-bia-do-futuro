🗂 Base de Conhecimento
•	transacoes.csv → hábitos de consumo e saldo.
•	historico_atendimento.csv → consistência nas respostas.
•	perfil_investidor.json → perfil de risco e objetivos.
•	produtos_financeiros.json → catálogo de produtos financeiros.
🤖 Agente FinFree
•	Carrega os dados da base.
•	Monta o contexto do cliente.
•	Aplica regras (50-30-20, perfil de risco, simulações).
•	Gera resposta personalizada.
👤 Usuário
•	Faz uma pergunta ou solicitação.
•	Recebe uma resposta clara, confiável e adaptada ao seu perfil.
---
📄 Exemplo de Contexto Montado
Dados do Cliente:
- Nome: Maria
- Perfil: Conservador
- Renda mensal: R$ 3.000
- Objetivo: Intercâmbio em 2 anos

Últimas transações:
- 01/03: Salário +R$ 3.000
- 05/03: Aluguel -R$ 1.200
- 07/03: Supermercado -R$ 400
- 10/03: Investimento Tesouro Selic -R$ 500
- 15/03: Freelance +R$ 800

Produtos disponíveis:
- Tesouro Selic: risco baixo, liquidez diária
- CDB: risco baixo, liquidez prazo definido
- LCI: risco baixo, isento de IR, prazo definido
- ETF: risco médio, liquidez diária
________________________________________
