# mcp_server/api.py

from fastapi import APIRouter, Request
from datetime import datetime
import os
import json

# ─── Ejecución y registro ─────────────────────────────────────
from executors.registry import ejecutar_tool
from utils.commands import registrar_accion

# ─── Heartbeat y cola ─────────────────────────────────────────
from heartbeat.heartbeat_tracker import actualizar_ping, listar_nodos
from task_queue.memory_queue import agregar_tarea, obtener_tareas, tareas_pendientes

router = APIRouter()

# ───────────────────────────────────────────────────────────────
# Ejecutar herramientas: GET /tools/{tool}?param1=...&param2=...
# ───────────────────────────────────────────────────────────────
@router.get("/tools/{tool_name}")
async def api_ejecutar_tool(tool_name: str, request: Request):
    params = dict(request.query_params)
    registrar_accion(tool_name, params)
    resultado = ejecutar_tool(tool_name, params)
    return {"result": resultado}

# ───────────────────────────────────────────────────────────────
# Recibir status.json desde agentes/demonio → POST /status
# ───────────────────────────────────────────────────────────────
@router.post("/status")
async def api_guardar_status(data: dict):
    os.makedirs("data", exist_ok=True)
    with open("data/status.json", "w") as f:
        json.dump(data, f, indent=2)
    return {"message": "Status recibido correctamente"}

# ───────────────────────────────────────────────────────────────
# Consultar el último status recibido → GET /status
# ───────────────────────────────────────────────────────────────
@router.get("/status")
def api_leer_status():
    try:
        with open("data/status.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "Aún no se ha recibido status.json"}

# ───────────────────────────────────────────────────────────────
# Heartbeat: Agentes vivos → POST /heartbeat + GET /heartbeat
# ───────────────────────────────────────────────────────────────
@router.post("/heartbeat")
def recibir_ping(data: dict):
    ip = data.get("ip")
    hostname = data.get("hostname", "desconocido")
    if ip:
        actualizar_ping(ip, hostname)
        return {"message": "Ping registrado"}
    return {"error": "Falta IP"}

@router.get("/heartbeat")
def ver_estado_nodos():
    return listar_nodos()

# ───────────────────────────────────────────────────────────────
# Cola de tareas: Agentes remotos → POST/GET /queue/{ip}
# ───────────────────────────────────────────────────────────────
@router.post("/queue/{ip}")
def enviar_comando(ip: str, datos: dict):
    accion = datos.get("accion")
    parametros = datos.get("parametros", {})
    if accion:
        agregar_tarea(ip, accion, parametros)
        return {"message": "Tarea añadida"}
    return {"error": "Falta acción"}

@router.get("/queue/{ip}")
def recibir_comandos(ip: str):
    return {"tareas": obtener_tareas(ip)}

@router.get("/queue/{ip}/pendientes")
def contar_comandos(ip: str):
    return {"pendientes": tareas_pendientes(ip)}
