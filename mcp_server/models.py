# mcp_server/models.py

from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

# ─────────────────────────────────────────────
# Modelo de proceso activo en el sistema
# ─────────────────────────────────────────────
class Proceso(BaseModel):
    pid: int
    name: str
    memory_percent: float

# ─────────────────────────────────────────────
# Modelo del estado del servidor (status.json)
# ─────────────────────────────────────────────
class EstadoServidor(BaseModel):
    timestamp: str
    hostname: str
    os: str

    cpu_usage_percent: float
    ram_usage_percent: float
    disk_usage_percent: float

    total_processes: int
    top_memory_processes: List[Proceso]
    running_users: List[str]

    network_connections: int
    active_ports: List[int]
    interfaces: Dict[str, Dict]

    recent_log_errors: Optional[int]
    failed_logins: Optional[int]
    malware_score: Optional[float]
    suspicious_ips: Optional[List[str]]
    top_ports: Optional[Dict[str, int]]
    avg_ping_ms: Optional[float]
    file_hashes: Optional[Dict[str, str]]

# ─────────────────────────────────────────────
# Modelo de acción ejecutada (para registrar)
# ─────────────────────────────────────────────
class AccionEjecutada(BaseModel):
    timestamp: datetime
    herramienta: str
    parametros: Dict[str, str]
    resultado: str
