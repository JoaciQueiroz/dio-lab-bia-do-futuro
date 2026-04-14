import streamlit as st
from finfree.agente import carregar_dados, montar_contexto, definir_system_prompt, chamar_ollama

st.set_page_config(page_title="FinFree AI", layout="centered")
st.title("💸 FinFree - Agente Financeiro")

# 1. Carregar dados e contexto
transacoes, historico, perfil, produtos, metas, alertas = carregar_dados()
contexto = montar_contexto(transacoes, historico, perfil, produtos, metas, alertas)
system_prompt = definir_system_prompt()

# 2. Inicializar histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Mostrar histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Entrada do usuário
if pergunta := st.chat_input("Como posso ajudar seu bolso hoje?"):
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    with st.chat_message("assistant"):
        with st.spinner("Analisando dados..."):
            resposta = chamar_ollama(system_prompt, contexto, pergunta)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
