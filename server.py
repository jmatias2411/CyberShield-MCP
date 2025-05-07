### Estructura modular de un servidor MCP para ciberseguridad en Windows

# server.py
from mcp.server.fastmcp import FastMCP
from tools.firewall import block_port, block_ip, unblock_port, unblock_ip, list_firewall_rules
from tools.diagnostics import do_ping, scan_network
from tools.logs import analyze_logs
from tools.hardening import disable_network_discovery, list_local_users, show_password_policy
from tools.agent_response import auto_block_ip, get_defense_log, quarantine_mode
from tools.processes import list_processes, list_suspicious_processes, kill_process
from tools.network_watch import list_active_connections, detect_suspicious_ips
from tools.eventlog_analyzer import get_recent_failed_logins, get_privilege_changes
from resources.firewall_state import get_firewall_rules
from prompts.threat_response import suggest_block_action
from tools.agent_response import system_diagnostic_summary

mcp = FastMCP("CyberShield Agent")

# Registro de herramientas
mcp.tool()(block_port)
mcp.tool()(block_ip)
mcp.tool()(unblock_port)
mcp.tool()(unblock_ip)
mcp.tool()(list_firewall_rules)
mcp.tool()(do_ping)
mcp.tool()(scan_network)
mcp.tool()(analyze_logs)
mcp.tool()(disable_network_discovery)
mcp.tool()(list_local_users)
mcp.tool()(show_password_policy)
mcp.tool()(auto_block_ip)
mcp.tool()(quarantine_mode)
mcp.tool()(list_processes)
mcp.tool()(list_suspicious_processes)
mcp.tool()(kill_process)
mcp.tool()(list_active_connections)
mcp.tool()(detect_suspicious_ips)
mcp.tool()(get_recent_failed_logins)
mcp.tool()(get_privilege_changes)
mcp.tool()(system_diagnostic_summary)

# Registro de recursos
mcp.resource("firewall://rules")(get_firewall_rules)
mcp.resource("log://defense")(get_defense_log)

# Registro de prompts
mcp.prompt()(suggest_block_action)