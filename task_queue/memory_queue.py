# queue/memory_queue.py

from collections import defaultdict
import threading

cola = defaultdict(list)
lock = threading.Lock()

def agregar_tarea(ip: str, accion: str, parametros: dict):
    with lock:
        cola[ip].append({
            "accion": accion,
            "parametros": parametros
        })

def obtener_tareas(ip: str) -> list:
    with lock:
        tareas = cola.get(ip, [])
        cola[ip] = []  # limpiar después de devolver
        return tareas

def tareas_pendientes(ip: str) -> int:
    with lock:
        return len(cola.get(ip, []))
