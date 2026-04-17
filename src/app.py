import streamlit as st
from agente import gerar_resposta

st.title("💰 Clara: Sua Assistente Financeira")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Como posso ajudar?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        resposta = gerar_resposta(prompt)
        st.markdown(resposta)
    st.session_state.messages.append({"role": "assistant", "content": resposta})