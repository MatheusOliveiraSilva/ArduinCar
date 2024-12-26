import streamlit as st
import asyncio
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from led_agent_graph import get_graph

graph = get_graph()

config = {"configurable": {"thread_id": "100"}}

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("Controle de LED com Assistente Virtual")

st.subheader("Histórico de Conversas:")
for msg in st.session_state["messages"]:

    if isinstance(msg, HumanMessage):
        st.write(f"Eu: {msg.content}")

    if isinstance(msg, AIMessage):
        st.write(f"Assistente: {msg.content}")

st.subheader("Envie um Comando:")
command = st.text_input("Digite o comando para o assistente:")

async def send_to_graph(command):
    query = {"messages": command}

    result = graph.invoke(query, config)

    last_msg = result["messages"][-1]

    st.session_state["messages"].append(last_msg)
    st.rerun()

if st.button("Enviar"):
    if command:
        st.session_state["messages"].append(HumanMessage(content=command))
        asyncio.run(send_to_graph([HumanMessage(content=command)]))
