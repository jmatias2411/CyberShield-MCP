# mcp_server/websocket.py

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from datetime import datetime
from typing import List 

ws_router = APIRouter()
conexiones_activas: List[WebSocket] = []

@ws_router.websocket("/ws/events")
async def websocket_eventos(websocket: WebSocket):
    await websocket.accept()
    conexiones_activas.append(websocket)
    print(f"🔌 Cliente conectado: {websocket.client}")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"📨 Mensaje recibido: {data}")
            await websocket.send_text(f"🔁 Eco: {data}")
    except WebSocketDisconnect:
        print(f"❌ Cliente desconectado: {websocket.client}")
        conexiones_activas.remove(websocket)

# 🔔 Función auxiliar para enviar mensajes a todos los conectados
async def notificar_todos(mensaje: str):
    for ws in conexiones_activas:
        try:
            await ws.send_text(f"📢 {datetime.now().isoformat()} → {mensaje}")
        except:
            pass  # Silenciar errores de conexión
