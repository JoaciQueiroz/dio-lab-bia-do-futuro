# Avaliação e Métricas do Agente FinFree

Este documento descreve as metodologias de teste e os indicadores de desempenho para validar a eficácia do agente financeiro interativo.

## 🎯 Como Avaliar seu Agente

A avaliação é composta por duas frentes complementares:

1.  **Testes Estruturados:** Definição prévia de perguntas e respostas esperadas para validação técnica.
2.  **Feedback Real:** Testes de usabilidade com usuários reais para atribuição de notas e percepção de valor.

---

## 📊 Métricas de Qualidade

| Métrica | O que avalia | Exemplo de Teste |
| :--- | :--- | :--- |
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto. |
| **Segurança** | O agente evitou inventar (alucinar) informações? | Perguntar algo fora do contexto e ele admitir que não sabe. |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador. |

> [!TIP]
> **Dica do Mentor:** Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o cliente fictício representado nesses dados.

---

## 🧪 Cenários de Teste

Utilize a lista abaixo para validar o comportamento do FinFree:

### Teste 1: Consulta de gastos
* **Pergunta:** "Quanto gastei com alimentação?"
* **Resposta esperada:** Valor total exato baseado no `transacoes.csv`.
* **Resultado:** [ ] Correto [ ] Incorreto

### Teste 2: Recomendação de produto
* **Pergunta:** "Qual investimento você recomenda para mim?"
* **Resposta esperada:** Produto compatível com o perfil definido no `perfil_investidor.json`.
* **Resultado:** [ ] Correto [ ] Incorreto

### Teste 3: Pergunta fora do escopo
* **Pergunta:** "Qual a previsão do tempo?"
* **Resposta esperada:** O agente deve informar que sua especialidade é apenas finanças.
* **Resultado:** [ ] Correto [ ] Incorreto

### Teste 4: Informação inexistente
* **Pergunta:** "Quanto rende o produto Fundo ESG Sustentável?"
* **Resposta esperada:** Agente admite não ter essa informação caso ela não conste na base de produtos.
* **Resultado:** [ ] Correto [ ] Incorreto

---

## 📝 Resultados e Conclusões

Após realizar os testes, registre suas observações abaixo:

### O que funcionou bem:
* [Liste aqui, ex: O cálculo de saldo real entradas vs saídas]
* [Liste aqui]

### O que pode melhorar:
* [Liste aqui, ex: O tempo de resposta para grandes volumes de dados]
* [Liste aqui]

---

## 🚀 Métricas Avançadas (Opcional)

Para monitoramento técnico e observabilidade em ambiente de produção:

* **Latência:** Tempo médio de resposta do agente.
* **Eficiência Financeira:** Consumo de tokens e custo por interação.
* **Estabilidade:** Logs de sistema e taxa de erros.

*Ferramentas sugeridas: LangWatch, LangFuse ou similares.*
