# heartbeat/heartbeat_tracker.py

from datetime import datetime, timedelta
import threading

# Diccionario en memoria: {ip: {last_seen, hostname, status}}
nodos = {}
lock = threading.Lock()
TIEMPO_MUERTO = 60  # segundos sin ping = inactivo

def actualizar_ping(ip: str, hostname: str):
    with lock:
        nodos[ip] = {
            "hostname": hostname,
            "last_seen": datetime.now().isoformat(),
            "status": "alive"
        }

def listar_nodos():
    with lock:
        ahora = datetime.now()
        estado_actualizado = {}

        for ip, datos in nodos.items():
            ultima = datetime.fromisoformat(datos["last_seen"])
            activo = (ahora - ultima) < timedelta(seconds=TIEMPO_MUERTO)
            estado_actualizado[ip] = {
                "hostname": datos["hostname"],
                "last_seen": datos["last_seen"],
                "status": "alive" if activo else "inactive"
            }

        return estado_actualizado
