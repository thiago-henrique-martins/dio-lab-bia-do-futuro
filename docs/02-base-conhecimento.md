# Base de Conhecimento

## Dados Utilizados

Foram utilizados os dados mockados disponibilizados pela plataforma na pasta `data/` para garantir a execução do desafio. A utilização foi dividida da seguinte forma:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, permitindo que a Clara mantenha a continuidade do atendimento e demonstre empatia com dúvidas passadas. |
| `perfil_investidor.json` | JSON | Identificar o nível de aversão a risco e as metas do usuário (ex: montar reserva de emergência) para guiar o tom da conversa. |
| `produtos_financeiros.json` | JSON | Filtrar e sugerir produtos conservadores e de renda fixa adequados ao perfil do usuário, respeitando a regra de não recomendar renda variável. |
| `transacoes.csv` | CSV | Realizar a leitura dinâmica do padrão de gastos, permitindo que a Clara categorize despesas e emita alertas proativos de orçamento. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Para manter a integridade do desafio, os arquivos originais foram mantidos em sua essência. A principal adaptação lógica foi criar um filtro no código para que o arquivo `produtos_financeiros.json` exponha à Clara apenas opções de baixo risco (como Tesouro Direto, CDBs e fundos de renda fixa), garantindo que ela não quebre sua limitação de fazer *stock picking* ou sugerir investimentos arriscados.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV são carregados em memória no início da sessão através de bibliotecas de manipulação de dados (como o Pandas). Eles são mantidos em cache pela interface para garantir consultas rápidas e sem atrasos durante a interação.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

A integração ocorre de forma híbrida:
1. **System Prompt:** Informações estáticas, como o nome do usuário extraído do `perfil_investidor.json`, vão direto na instrução inicial para definir o tom de voz e a personalização da Clara.
2. **Injeção Dinâmica:** Os dados massivos, como as linhas do `transacoes.csv`, são formatados e injetados no prompt do LLM (Gemini) apenas quando o usuário faz uma pergunta relacionada a gastos ou quando a Clara precisa verificar se um alerta de orçamento deve ser disparado.

---

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```text
INSTRUÇÕES DO SISTEMA:
Você é a Clara, uma assistente financeira amigável e educativa. Responda com base nos dados fornecidos abaixo. Seu objetivo é ajudar o usuário a organizar as contas e poupar. Não sugira investimentos de alto risco ou renda variável.

DADOS DO CLIENTE:
- Nome: Thiago
- Perfil: Conservador (Foco em Reserva de Emergência)
- Meta de economia mensal: R$ 300,00

RESUMO DE GASTOS (Últimos 7 dias):
- 08/04: Alimentação (iFood) - R$ 85,00
- 10/04: Assinaturas (Netflix) - R$ 39,90
- 12/04: Transporte (Combustível) - R$ 150,00
- 14/04: Alimentação (Supermercado) - R$ 120,00

PERGUNTA DO USUÁRIO:
"Clara, como estão meus gastos com comida essa semana?"
