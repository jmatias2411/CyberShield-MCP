# fastapi_mcp_server.py

from fastapi import FastAPI, Request
import os
import json

# ─── Herramientas MCP ──────────────────────────────────────────
from tools.firewall import block_port, block_ip, unblock_port, unblock_ip, list_firewall_rules
from tools.diagnostics import do_ping, scan_network
from tools.logs import analyze_logs
from tools.hardening import disable_network_discovery, list_local_users, show_password_policy
from tools.agent_response import auto_block_ip, get_defense_log, quarantine_mode, system_diagnostic_summary
from tools.processes import list_processes, list_suspicious_processes, kill_process
from tools.network_watch import list_active_connections, detect_suspicious_ips
from tools.eventlog_analyzer import get_recent_failed_logins, get_privilege_changes

# ─── App FastAPI ───────────────────────────────────────────────
app = FastAPI(title="CyberShield MCP", description="Servidor MCP con herramientas defensivas")

# ─── FIREWALL ───────────────────────────────────────────────────
@app.get("/tools/block_port")
def api_block_port(port: int):
    return {"result": block_port(port)}

@app.get("/tools/unblock_port")
def api_unblock_port(port: int):
    return {"result": unblock_port(port)}

@app.get("/tools/block_ip")
def api_block_ip(ip: str):
    return {"result": block_ip(ip)}

@app.get("/tools/unblock_ip")
def api_unblock_ip(ip: str):
    return {"result": unblock_ip(ip)}

@app.get("/tools/list_firewall_rules")
def api_list_firewall_rules():
    return {"result": list_firewall_rules()}

# ─── RED ────────────────────────────────────────────────────────
@app.get("/tools/ping")
def api_do_ping(host: str):
    return {"result": do_ping(host)}

@app.get("/tools/scan_network")
def api_scan_network(base_ip: str):
    return {"result": scan_network(base_ip)}

# ─── HARDENING ──────────────────────────────────────────────────
@app.get("/tools/disable_network_discovery")
def api_disable_discovery():
    return {"result": disable_network_discovery()}

@app.get("/tools/list_local_users")
def api_list_users():
    return {"result": list_local_users()}

@app.get("/tools/password_policy")
def api_password_policy():
    return {"result": show_password_policy()}

# ─── PROCESOS ───────────────────────────────────────────────────
@app.get("/tools/list_processes")
def api_list_processes():
    return {"result": list_processes()}

@app.get("/tools/list_suspicious_processes")
def api_list_sus_procs():
    return {"result": list_suspicious_processes()}

@app.get("/tools/kill_process")
def api_kill_process(name: str):
    return {"result": kill_process(name)}

# ─── NETWORK WATCH ──────────────────────────────────────────────
@app.get("/tools/active_connections")
def api_active_connections():
    return {"result": list_active_connections()}

@app.get("/tools/suspicious_ips")
def api_suspicious_ips():
    return {"result": detect_suspicious_ips()}

# ─── EVENTOS DE SEGURIDAD ───────────────────────────────────────
@app.get("/tools/failed_logins")
def api_failed_logins():
    return {"result": get_recent_failed_logins()}

@app.get("/tools/privilege_changes")
def api_privilege_changes():
    return {"result": get_privilege_changes()}

# ─── DEFENSA INTELIGENTE ────────────────────────────────────────
@app.get("/tools/auto_block_ip")
def api_auto_block(ip: str):
    return {"result": auto_block_ip(ip)}

@app.get("/tools/quarantine_mode")
def api_quarantine():
    return {"result": quarantine_mode()}

@app.get("/tools/system_diagnostic")
def api_system_diagnostic():
    return {"result": system_diagnostic_summary()}

# ─── LOG DE DEFENSA ─────────────────────────────────────────────
@app.get("/resources/defense_log")
def api_get_defense_log():
    return {"result": get_defense_log()}

# ─── STATUS (desde agentes) ─────────────────────────────────────
@app.post("/status")
async def recibir_status(data: dict):
    os.makedirs("data", exist_ok=True)
    with open("data/status.json", "w") as f:
        json.dump(data, f, indent=2)
    return {"message": "Status recibido"}

@app.get("/status")
def devolver_status():
    try:
        with open("data/status.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "status.json no encontrado"}
