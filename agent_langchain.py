from langchain.agents import initialize_agent, Tool
from langchain.llms import Ollama
import requests

# Instancia del modelo local con Ollama
llm = Ollama(model="mistral")  # Cambia a llama2, codellama, etc. según lo que tengas

# Herramientas conectadas al servidor FastAPI (MCP)
def auto_block(ip: str) -> str:
    response = requests.get("http://localhost:4242/tools/auto_block_ip", params={"ip": ip})
    return response.json()["result"]

def diagnostic() -> str:
    response = requests.get("http://localhost:4242/tools/system_diagnostic")
    return response.json()["result"]

def list_suspicious() -> str:
    response = requests.get("http://localhost:4242/tools/list_suspicious_processes")
    return response.json()["result"]

# Definir herramientas LangChain
tools = [
    Tool(
        name="bloquear ip automáticamente",
        func=auto_block,
        description="Usa esta herramienta para bloquear una IP sospechosa que se detecte en el análisis."
    ),
    Tool(
        name="diagnóstico del sistema",
        func=diagnostic,
        description="Realiza un resumen completo del estado de seguridad del sistema: procesos, red y eventos."
    ),
    Tool(
        name="listar procesos sospechosos",
        func=list_suspicious,
        description="Muestra una lista de procesos sin ruta o potencialmente maliciosos activos en el sistema."
    )
]


# Inicializar agente con razonamiento de cero (react)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",
    verbose=True
)

# Prompt de ejemplo
agent.run("¿Hay procesos sospechosos activos? Si es así, haz un diagnóstico del sistema.")
