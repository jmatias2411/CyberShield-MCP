"""
CyberShield IA - Agente de prueba para el servidor MCP
Este agente usa LangChain y Ollama (LLaMA 2) para interactuar con herramientas registradas en el MCP.

Objetivo: Demostrar cómo un LLM puede invocar funciones MCP a partir de lenguaje natural.
"""

import streamlit as st
from langchain.agents import initialize_agent, Tool
from langchain_community.llms.ollama import Ollama
import requests

# 🧠 Instancia del modelo local
llm = Ollama(model="llama2")  # Asegúrate de que está cargado en Ollama

# 🌐 URL base del servidor FastAPI MCP
BASE_URL = "http://localhost:4242"

# 🔧 Utilidades para llamar al servidor FastAPI
def call_tool(endpoint: str, params: dict = None) -> str:
    try:
        response = requests.get(f"{BASE_URL}/tools/{endpoint}", params=params or {})
        response.raise_for_status()
        return response.json()["result"]
    except Exception as e:
        return f"Error al llamar a {endpoint}: {e}"

# 🛠️ Definición de herramientas mínimas para test
tools = [
    Tool("listar procesos", lambda _: call_tool("list_processes"), "Muestra los procesos actualmente en ejecución"),
    Tool("hacer ping", lambda ip: call_tool("ping", {"host": ip}), "Haz ping a una dirección IP"),
    Tool("bloquear ip", lambda ip: call_tool("block_ip", {"ip": ip}), "Bloquea una IP usando el firewall"),
    Tool("diagnóstico del sistema", lambda _: call_tool("system_diagnostic"), "Ejecuta un resumen de diagnóstico del sistema"),
]

# 📝 Prompt breve
prefix = """
Eres CyberShield, un asistente de ciberseguridad conectado a un servidor MCP.
Tu función es ejecutar herramientas como 'listar procesos', 'hacer ping', o 'bloquear IP' cuando el usuario te lo indique.
Usa solo las herramientas disponibles y responde con claridad y precisión.
"""

# 🤖 Inicializar agente
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=True,
    agent_kwargs={"prefix": prefix},
    handle_parsing_errors=True,
    max_iterations=3,
    max_execution_time=20
)

# 🖼️ Interfaz Streamlit
st.set_page_config(page_title="CyberShield IA (Test)", page_icon="🛡️")
st.title("🛡️ CyberShield IA — Agente de Prueba MCP")
st.write("Agente de prueba para ejecutar herramientas del servidor MCP.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("¿Qué acción querés ejecutar en el servidor MCP?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    try:
        result = agent.run(user_input)
    except Exception as e:
        result = f"❌ Error al procesar: {e}"
    st.session_state.messages.append({"role": "assistant", "content": result})
    with st.chat_message("assistant"):
        st.markdown(result)
