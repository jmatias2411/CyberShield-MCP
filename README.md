# 🛡️ CyberShield MCP — Servidor MCP de Defensa Autónoma (Windows)

**CyberShield MCP** es un **servidor MCP (Model Context Protocol)** completamente funcional diseñado para ejecutar herramientas defensivas, consultar recursos del sistema y tomar decisiones de seguridad con apoyo de inteligencia artificial.

Funciona sobre **Windows**, expone comandos críticos del sistema de forma segura, y puede ser controlado desde **Claude Desktop** o mediante **agentes LangChain**, creando así una defensa **contextual, precisa y autónoma**.

---

## ⚙️ Requisitos y dependencias

> 💡 **Solo compatible con Windows** por ahora (utiliza `netsh`, `whoami`, `wmic`, etc.)

Instalación rápida:

```bash
pip install mcp[cli] langchain langchain-mcp-adapters langchain-ollama
```

Si usás variables de entorno en `.env`, ejecutá:

```bash
mcp install -f
```

---

## 🚀 Tecnologías utilizadas

* 🧠 **Model Context Protocol (MCP)** — para exponer herramientas y prompts a modelos de lenguaje
* 🖥️ **Claude Desktop** — para interacción natural con herramientas defensivas
* 🧱 **LangChain** — integración con agentes IA autónomos
* 🐍 **Python 3.10+** — servidor principal
* 🔄 **Subprocess seguro** — para ejecución controlada del sistema operativo
* 🧪 **MCP Inspector** — para testeo y depuración visual de herramientas y flujos

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
│   ├── hardening.py        # Fortalecimiento del sistema (descubrimiento, usuarios, contraseñas)
│   └── agent_response.py   # Acciones automáticas: bloqueo, modo cuarentena, logs de defensa
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
│   └── commands.py         # Funciones comunes de ejecución (subprocess seguro)
```

---

## 🤖 Usos prácticos con IA

### 🧠 Claude Desktop

Preguntas posibles:

```
Haz ping a 8.8.8.8  
Muéstrame las reglas del firewall  
¿Estoy bajo ataque?  
Bloquea la IP 192.168.1.42  
Desactiva el descubrimiento de red  
Muestra los usuarios locales
```

### 🔗 Agentes IA con LangChain

```python
from langchain_mcp.adapters import MCPToolAdapter

tools = MCPToolAdapter.load_tools_from_server("http://localhost:8000")
```

Perfecto para integrarlo en asistentes defensivos, flujos autónomos o sistemas RAG con control del sistema operativo.

---

## 🧪 Testing con MCP Inspector

> ¿Querés ver qué está pasando bajo el capó?
> Activá el **Inspector de MCP** y vas a poder:

* Ver funciones ejecutadas
* Monitorear argumentos recibidos
* Depurar errores rápidamente
* Confirmar rutas de activación

Simplemente corré tu servidor con:

```bash
uv run mcp dev server.py
```

Y abrí el **Inspector Web** cuando interactúes con Claude o LangChain.

---

## 💬 Ejemplos de uso

### 🛠 `@tool`: `do_ping(host: str)`

```
Haz ping a 8.8.8.8
```

### 📦 `@resource`: `firewall://rules`

```
Muéstrame las reglas activas del firewall.
```

### 🧠 `@prompt`: `suggest_block_action(threat_description)`

```
He detectado múltiples conexiones sospechosas desde 192.168.1.42. ¿Qué debería hacer?
```

---

## 🧰 Modo CLI

Si querés probar sin IA, podés ejecutar cualquier herramienta desde consola mientras desarrollás:

```bash
python tools/diagnostics.py
```

(Podés agregar fácilmente una CLI de testing o una GUI rápida en Streamlit si querés más control.)

---

## 🔐 ¿Qué podés hacer con CyberShield MCP?

* Automatizar defensa en sistemas Windows
* Ejecutar comandos críticos mediante IA
* Fortalecer el sistema y reducir superficie de ataque
* Coordinar respuestas desde agentes IA o modelos conversacionales
* Crear un sistema híbrido: humano + máquina, donde la IA te sugiere y ejecuta

---

¿Listo para una defensa con cerebro?
Clonalo, conectalo con Claude o tu agente LangChain, y empezá a blindar tu sistema. 💥
