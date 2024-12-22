import streamlit as st
import asyncio
from langchain_core.messages import HumanMessage
from langgraph_sdk import get_client

# Configuração do cliente LangGraph
URL = "http://localhost:59974"
client = get_client(url=URL)
assistant = "led_agent_graph"

# Inicializa o estado da sessão
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "thread_id" not in st.session_state:
    thread = asyncio.run(client.threads.create())
    st.session_state["thread_id"] = thread["thread_id"]

# Título do app
st.title("Controle de LED com Assistente Virtual")

# Mostra o histórico de mensagens
st.subheader("Histórico de Conversas:")
for msg in st.session_state["messages"]:
    role = "Usuário" if isinstance(msg, HumanMessage) else "Assistente"
    st.markdown(f"**{role}:** {msg['content']}")

# Campo de entrada para enviar comandos
st.subheader("Envie um Comando:")
command = st.text_input("Digite o comando para o assistente:")

# Função para processar o comando assíncrono
async def send_to_graph(command):
    query = {"messages": [HumanMessage(content=command)]}

    last_msg = None
    async for chunk in client.runs.stream(
            st.session_state["thread_id"],
            assistant,
            input=query,
            stream_mode="values"):
        if chunk.data and chunk.event != "metadata":
            last_msg = chunk.data["messages"][-1]

    st.session_state["messages"].append(last_msg)
    st.rerun()

# Processa o comando ao clicar no botão
if st.button("Enviar"):
    if command:
        # Adiciona a mensagem do usuário ao histórico
        st.session_state["messages"].append({"content": command, "role": "user"})
        asyncio.run(send_to_graph(command))
