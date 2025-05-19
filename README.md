[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/jmatias2411-cybershield-mcp-badge.png)](https://mseep.ai/app/jmatias2411-cybershield-mcp)

# 🛡️ CyberShield MCP — Servidor MCP de Defensa Autónoma (Windows)

CyberShield MCP es un servidor MCP (Model Context Protocol) completamente funcional diseñado para ejecutar herramientas defensivas, consultar recursos del sistema y tomar decisiones de seguridad con apoyo de inteligencia artificial.

Funciona sobre Windows, expone comandos críticos del sistema de forma segura, y puede ser controlado desde Claude Desktop o mediante agentes LangChain, creando así una defensa contextual, precisa y autónoma.

---

## ⚙️ Requisitos y dependencias

💡 Solo compatible con Windows por ahora (utiliza `netsh`, `ping`, `Get-WinEvent`, etc.)

Instalación rápida:

```bash
pip install mcp[cli] langchain langchain-ollama fastapi uvicorn requests
```

Si usás variables de entorno en `.env`, ejecutá:

```bash
mcp install -f
```

---

## 📂 Estructura del proyecto

```
cybershield_mcp/
├── server.py               # Punto de entrada principal
├── pyproject.toml          # Configuración del proyecto (con uv o poetry)
├── README.md               # Descripción del proyecto
├── .env                    # Variables de entorno (si usás `mcp install -f`)
│
├── tools/                  # Herramientas de defensa y diagnóstico
│   ├── __init__.py
│   ├── firewall.py         # Bloqueo y desbloqueo de puertos/IPs
│   ├── diagnostics.py      # Ping y escaneo con nmap
│   ├── logs.py             # Análisis de logs con Context
│   ├── hardening.py        # Fortalecimiento del sistema
│   ├── agent_response.py   # Acciones automáticas y diagnóstico rápido
│   ├── network_watch.py    # Conexiones activas y detección de IPs raras
│   ├── eventlog_analyzer.py # Revisión de eventos de seguridad (logins fallidos, privilegios)
│   └── processes.py        # Escaneo y gestión de procesos activos
│
├── resources/
│   ├── __init__.py
│   └── firewall_state.py   # Consulta del estado actual del firewall
│
├── prompts/
│   ├── __init__.py
│   └── threat_response.py  # Prompt para decidir acción ante amenazas
│
├── utils/
│   ├── __init__.py
│   └── commands.py         # Funciones comunes para subprocess seguro
│
├── fastapi_mcp_server.py   # Exposición HTTP de herramientas MCP para integración externa
├── agent_langchain.py      # Agente IA con LangChain + Ollama usando MCP vía FastAPI
├── Dockerfile              # Imagen Docker del servidor FastAPI
├── docker-compose.yml      # Despliegue simplificado con Docker Compose
```

---

## 🧠 Modos de uso con IA

### 🧠 Claude Desktop

1. Instalar tu servidor en Claude:
```bash
uv run mcp install server.py --name "CyberShield Agent"
```

2. Ejecutar el servidor MCP:
```bash
uv run mcp dev server.py
```

3. Claude ahora podrá usar frases como:
- "Haz ping a 8.8.8.8"
- "Bloquea la IP 192.168.1.50"
- "Activa el modo cuarentena"
- "¿Estoy bajo ataque?"

---

### 🔗 LangChain + Ollama (modo agente autónomo)

1. Levantar el servidor FastAPI:
```bash
uvicorn fastapi_mcp_server:app --port 4242
```

2. Usar `agent_langchain.py` para lanzar un agente con herramientas como:
- `bloquear ip automáticamente`
- `diagnóstico del sistema`
- `listar procesos sospechosos`

```bash
python agent_langchain.py
```

3. El agente decidirá con tu LLM cuándo ejecutar herramientas defensivas (bloqueo, diagnóstico, etc.)

---

## 🐳 Integración con Docker

### Dockerfile

Ya incluido en el proyecto. Crea una imagen del servidor FastAPI para correr en cualquier entorno.

### Para construir y correr:
```bash
docker build -t cybershield-api .
docker run -p 4242:4242 --name cybershield cybershield-api
```

### O con `docker-compose`:
```bash
docker-compose up --build
```

Esto te da:
- Reproducibilidad
- Despliegue rápido
- Entorno controlado
- Posibilidad de llevar tu MCP a servidores Linux sin instalación directa

---

## 🧪 Testing con MCP Inspector

Corré:
```bash
uv run mcp dev server.py
```
Y abrí el Inspector Web cuando interactúes con Claude o LangChain.

Podés ver:
- Funciones ejecutadas
- Argumentos pasados
- Tiempos de respuesta y errores

---

## 💬 Ejemplos rápidos (Claude o LangChain)

🛠 `@tool`: `do_ping(host: str)`
> "Haz ping a 8.8.8.8"

📦 `@resource`: `firewall://rules`
> "Muéstrame las reglas activas del firewall"

🧠 `@prompt`: `suggest_block_action(threat_description)`
> "He detectado conexiones sospechosas desde 192.168.1.42. ¿Qué debería hacer?"

🔗 `FastAPI`
> GET http://localhost:4242/tools/system_diagnostic

---

## 🧰 ¿Qué podés hacer con CyberShield MCP?

✅ Automatizar defensa en sistemas Windows  
✅ Ejecutar comandos críticos mediante IA  
✅ Fortalecer el sistema y reducir superficie de ataque  
✅ Coordinar respuestas desde agentes IA o modelos conversacionales  
✅ Exponer herramientas como endpoints HTTP para integraciones más amplias  
✅ Desplegarlo fácilmente en cualquier entorno con Docker

¿Listo para una defensa con cerebro? Clonalo, conectalo con Claude o tu agente LangChain, ¡y empezá a blindar tu sistema! 💥


[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/8f6b0a03-1593-4ed6-9d20-9e664f6c74e9)
