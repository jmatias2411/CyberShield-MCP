# tools/eventlog_analyzer.py

import subprocess

def get_recent_failed_logins(limit: int = 10) -> str:
    """
    Devuelve los últimos eventos de fallos de inicio de sesión (ID 4625).
    """
    try:
        ps_command = f"Get-WinEvent -FilterHashtable @{{LogName='Security'; ID=4625}} -MaxEvents {limit} | Format-List"
        result = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
        return result.stdout or "No se encontraron eventos de fallo de inicio de sesión."
    except Exception as e:
        return f"Error al obtener eventos de seguridad: {e}"

def get_privilege_changes(limit: int = 10) -> str:
    """
    Busca eventos relacionados con cambios de privilegios o elevación (ej: ID 4672).
    """
    try:
        ps_command = f"Get-WinEvent -FilterHashtable @{{LogName='Security'; ID=4672}} -MaxEvents {limit} | Format-List"
        result = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)
        return result.stdout or "No se encontraron eventos de privilegios elevados."
    except Exception as e:
        return f"Error al obtener eventos de privilegio: {e}"
