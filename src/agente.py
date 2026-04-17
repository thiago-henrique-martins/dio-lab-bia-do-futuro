import pandas as pd
import google.generativeai as genai
from config import GOOGLE_API_KEY

# Configuração do modelo Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Usando o modelo que funcionou no seu ambiente
model = genai.GenerativeModel('gemini-3-flash-preview')

def carregar_contexto_financeiro():
    """Lê os arquivos de dados para fornecer contexto à Clara."""
    try:
        df = pd.read_csv('data/transacoes.csv')
        # Pegamos o resumo das transações para a IA analisar
        resumo = df.to_string(index=False)
        return resumo
    except Exception as e:
        return f"Erro ao ler dados: {e}"

def gerar_resposta(pergunta):
    dados = carregar_contexto_financeiro()
    
    # System Prompt com Regras de Escopo e Dados Financeiros
    system_prompt = f"""
Você é a Clara, uma assistente especializada EXCLUSIVAMENTE em finanças pessoais.
Seu objetivo é analisar os dados financeiros fornecidos e dar conselhos baseados neles.

---
DADOS FINANCEIROS DO USUÁRIO:
{dados}
---

REGRA CRÍTICA DE ESCOPO:
1. Responda APENAS sobre finanças, economia, análise de gastos ou planejamento orçamentário.
2. Se o usuário perguntar sobre qualquer outro assunto (mecânica de moto, culinária, saúde, etc.), você DEVE recusar gentilmente dizendo: 
   "Sinto muito, mas meu conhecimento é restrito à sua vida financeira. Não posso te ajudar com assuntos fora de finanças, mas se quiser saber como esse possível gasto impacta seu orçamento, estou à disposição!"
3. Nunca saia do personagem de assistente financeira.
"""
    
    # Chamada do modelo unindo as regras, os dados e a pergunta do usuário
    response = model.generate_content(f"{system_prompt}\n\nPergunta do Usuário: {pergunta}")
    return response.text