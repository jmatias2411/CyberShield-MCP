# tools/processes.py

import subprocess

def list_processes() -> str:
    """
    Lista todos los procesos activos con su nombre e ID.
    """
    try:
        result = subprocess.run(["tasklist"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error al listar procesos: {e}"

def list_suspicious_processes() -> str:
    """
    Lista procesos sin ruta ejecutable (potencialmente ocultos o sospechosos).
    Requiere PowerShell.
    """
    try:
        ps_command = "Get-WmiObject Win32_Process | Where-Object { !$_.Path } | Select-Object Name, ProcessId"
        cmd = ["powershell", "-Command", ps_command]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout or "No se detectaron procesos sospechosos sin ruta."
    except Exception as e:
        return f"Error al escanear procesos sospechosos: {e}"

def kill_process(name: str) -> str:
    """
    Termina un proceso por nombre.
    """
    try:
        result = subprocess.run(["taskkill", "/F", "/IM", name], capture_output=True, text=True)
        return result.stdout or f"Proceso {name} terminado."
    except Exception as e:
        return f"Error al terminar proceso {name}: {e}"
