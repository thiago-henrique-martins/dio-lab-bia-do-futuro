# Código da Aplicação

Esta pasta contém o código-fonte do protótipo funcional da assistente financeira **Clara**. A aplicação foi projetada para ser modular, separando a interface do usuário da lógica de processamento de linguagem natural.

## Estrutura Sugerida

```text
src/
├── app.py              # Aplicação principal (Interface Streamlit)
├── agente.py           # Lógica do agente (Integração Gemini + Pandas)
├── config.py           # Configurações de segurança e variáveis de ambiente
└── requirements.txt    # Dependências do projeto
```

## Exemplo de requirements.txt

```
streamlit
google-generativeai
pandas
python-dotenv
```

## Como Rodar

```bash
# 1. Instalar as dependências do projeto
pip install -r requirements.txt

# 2. Configurar a chave de API
# Crie um arquivo .env na raiz do projeto com: GOOGLE_API_KEY=SUA_CHAVE_AQUI

# 3. Rodar a aplicação interativa
streamlit run src/app.py
```
## Observações e Aprendizados

> Registre aqui os ajustes que você fez no código e os motivos técnicos.

* **Segurança e Boas Práticas**: Implementei o gerenciamento de credenciais via arquivos `.env`. Como estudante de ADS, entendo que nunca devemos expor chaves de API em repositórios públicos, por isso utilizei a biblioteca `python-dotenv`.
* **Performance da LLM**: Optei por utilizar o **Pandas** para pré-processar os dados antes de enviá-los ao Gemini. Isso evita que o modelo receba informações irrelevantes, economiza tokens e torna a resposta da **Clara** muito mais precisa.
* **Modularização**: Separei a lógica do agente da interface do usuário. Essa organização facilita a manutenção do código e permite que a interface seja trocada no futuro (de Streamlit para uma página web completa, por exemplo) sem afetar a inteligência da assistente.
