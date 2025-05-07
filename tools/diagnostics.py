# tools/diagnostics.py

import subprocess

def do_ping(host: str) -> str:
    """
    Hace ping a un host (Windows CMD).
    Usa '-n' en lugar de '-c' para compatibilidad con Windows.
    """
    try:
        result = subprocess.run(
            ["ping", "-n", "4", host],
            capture_output=True,
            text=True
        )
        return result.stdout or "No se recibió respuesta del host."
    except Exception as e:
        return f"Error al hacer ping: {e}"

def scan_network(base_ip: str) -> str:
    """
    Escaneo de red básica usando nmap.
    Requiere tener nmap instalado y en el PATH.
    Escanea la subred completa /24 (ej: 192.168.1.0/24).
    """
    try:
        result = subprocess.run(
            ["nmap", "-sn", f"{base_ip}/24"],
            capture_output=True,
            text=True
        )
        return result.stdout or "No se encontraron dispositivos o nmap no está instalado."
    except FileNotFoundError:
        return "nmap no está instalado o no se encuentra en el PATH del sistema."
    except Exception as e:
        return f"Error al ejecutar el escaneo: {e}"
