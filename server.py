# server.py
"""
Registro modular de herramientas, recursos y prompts para CyberShield MCP.
Este archivo utiliza FastMCP como backend de ejecución.
"""

from mcp.server.fastmcp import FastMCP

# ─── Importar herramientas ─────────────────────────────────────
from tools.firewall import block_port, block_ip, unblock_port, unblock_ip, list_firewall_rules
from tools.diagnostics import do_ping, scan_network
from tools.logs import analyze_logs
from tools.hardening import disable_network_discovery, list_local_users, show_password_policy
from tools.agent_response import auto_block_ip, get_defense_log, quarantine_mode, system_diagnostic_summary
from tools.processes import list_processes, list_suspicious_processes, kill_process
from tools.network_watch import list_active_connections, detect_suspicious_ips
from tools.eventlog_analyzer import get_recent_failed_logins, get_privilege_changes

# ─── Importar recursos ─────────────────────────────────────────
from resources.firewall_state import get_firewall_rules

# ─── Importar prompts ──────────────────────────────────────────
from prompts.threat_response import suggest_block_action

# ─── Instancia del servidor MCP ───────────────────────────────
mcp = FastMCP("CyberShield MCP")

# ─── Registro de herramientas ─────────────────────────────────
for tool in [
    block_port, block_ip, unblock_port, unblock_ip,
    list_firewall_rules, do_ping, scan_network, analyze_logs,
    disable_network_discovery, list_local_users, show_password_policy,
    auto_block_ip, quarantine_mode, list_processes, list_suspicious_processes,
    kill_process, list_active_connections, detect_suspicious_ips,
    get_recent_failed_logins, get_privilege_changes, system_diagnostic_summary
]:
    mcp.tool()(tool)

# ─── Registro de recursos ──────────────────────────────────────
mcp.resource("firewall://rules")(get_firewall_rules)
mcp.resource("log://defense")(get_defense_log)

# ─── Registro de prompts ───────────────────────────────────────
mcp.prompt()(suggest_block_action)
