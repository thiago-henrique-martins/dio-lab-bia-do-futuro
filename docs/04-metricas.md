# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação e qual foi o maior gasto dessa categoria?"
- **Resposta esperada:** Valor baseado no `transacoes.csv` (R$ 570,00 total)
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Sobrou dinheiro este mês? O que você recomenda que eu faça com ele?"
- **Resposta esperada:** Cálculo do saldo (R$ 2.511,10) e recomendação de investimento/reserva.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** Agente informa que o conhecimento é restrito à vida financeira.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto eu gastei com farmácia ou remédios em outubro?"
- **Resposta esperada:** Localização exata da transação de R$ 89,00 no dia 07/10.
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após a bateria de testes, chegamos às seguintes conclusões:
**O que funcionou bem:**
- A integração entre o modelo Gemini 3 Flash e a biblioteca Pandas permitiu cálculos precisos sobre o CSV.

- O System Prompt foi eficiente em manter a Clara dentro do seu papel de especialista financeira, mesmo sob pressão de perguntas irrelevantes.

- A capacidade de sugerir próximos passos (como a reserva de emergência) agrega valor real ao usuário final.

**O que pode melhorar:**
- Latência: O tempo de resposta da API pode ser otimizado com técnicas de cache ou modelos menores para tarefas simples.
---

## Métricas Avançadas

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Tempo Médio de Resposta: ~2.5 segundos.
- 
- Consumo de Contexto: Eficiente, utilizando apenas as últimas 10 transações para análise rápida.
