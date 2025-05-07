# server.py
from mcp.server.fastmcp import FastMCP

# Importación de herramientas
from tools.firewall import block_port, block_ip
from tools.diagnostics import do_ping, scan_network
from tools.logs import analyze_logs

# Importación de recursos
from resources.firewall_state import get_firewall_rules

# Importación de prompts
from prompts.threat_response import suggest_block_action

# Crear instancia del servidor MCP
mcp = FastMCP("CyberShield Agent")

# Registrar herramientas
mcp.tool()(block_port)
mcp.tool()(block_ip)
mcp.tool()(do_ping)
mcp.tool()(scan_network)
mcp.tool()(analyze_logs)

# Registrar recursos
mcp.resource("firewall://rules")(get_firewall_rules)

# Registrar prompts
mcp.prompt()(suggest_block_action)
