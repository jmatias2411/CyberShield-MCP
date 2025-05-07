import subprocess
from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("CyberShield Agent")

# 🛠️ Herramientas

@mcp.tool()
def block_port(port: int) -> str:
    """Bloquea un puerto usando netsh (Windows Firewall)"""
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name=Block_Port_{port}", "dir=in", "action=block",
        "protocol=TCP", f"localport={port}"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"Puerto {port} bloqueado."

@mcp.tool()
def block_ip(ip: str) -> str:
    """Bloquea una IP remota en el firewall de Windows"""
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name=Block_IP_{ip}", "dir=in", "action=block",
        "remoteip=" + ip, "protocol=any"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"IP {ip} bloqueada."

@mcp.tool()
def do_ping(host: str) -> str:
    """Hace ping a un host desde Windows"""
    result = subprocess.run(["ping", "-n", "4", host], capture_output=True, text=True)
    return result.stdout

@mcp.tool()
def scan_network(base_ip: str) -> str:
    """Escaneo de red básico con nmap (requiere nmap instalado)"""
    result = subprocess.run(["nmap", "-sn", f"{base_ip}/24"], capture_output=True, text=True)
    return result.stdout or "Asegúrate de tener nmap instalado y en el PATH"

# 📦 Recurso
@mcp.resource("firewall://rules")
def get_firewall_rules() -> str:
    """Devuelve las reglas del firewall de Windows"""
    result = subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", "name=all"], capture_output=True, text=True)
    return result.stdout

# 🧠 Prompt
@mcp.prompt()
def suggest_block_action(threat_description: str) -> str:
    return (
        f"Se detectó una amenaza: {threat_description}.\n"
        "¿Qué acción deberíamos tomar? Opciones: bloquear IP, puerto, ignorar."
    )

# 📦 Context con logs
@mcp.tool()
async def analyze_logs(log_files: list[str], ctx: Context) -> str:
    for i, file in enumerate(log_files):
        ctx.info(f"Analizando {file}")
        await ctx.report_progress(i, len(log_files))
    return "Análisis finalizado"
