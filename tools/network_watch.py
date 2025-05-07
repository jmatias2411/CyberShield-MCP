# tools/network_watch.py

import subprocess

def list_active_connections() -> str:
    """
    Lista conexiones activas (establecidas) del sistema con IP remota y puerto.
    Usa netstat con flags -ano para mayor detalle.
    """
    try:
        result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error al obtener conexiones activas: {e}"

def detect_suspicious_ips(keywords: list[str] = ["185.", "89.", "ru", "cn"]) -> str:
    """
    Busca patrones sospechosos en las conexiones activas.
    Ej: IPs extranjeras o rangos raros.
    """
    try:
        result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        sospechosos = [line for line in lines if any(k in line for k in keywords)]
        return "\n".join(sospechosos) if sospechosos else "No se detectaron IPs sospechosas."
    except Exception as e:
        return f"Error al buscar IPs sospechosas: {e}"
