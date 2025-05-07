# tools/hardening.py

import subprocess

def disable_network_discovery() -> str:
    """
    Desactiva el descubrimiento de red en Windows.
    Útil para evitar que otros equipos vean este dispositivo en la red local.
    """
    try:
        cmd = [
            "powershell", "-Command",
            "Set-NetFirewallRule -DisplayGroup 'Network Discovery' -Enabled False"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout or "Descubrimiento de red desactivado."
    except Exception as e:
        return f"Error al desactivar el descubrimiento de red: {e}"

def list_local_users() -> str:
    """
    Lista los usuarios locales del sistema.
    Útil para auditorías de seguridad.
    """
    try:
        result = subprocess.run(["net", "user"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error al listar usuarios locales: {e}"

def show_password_policy() -> str:
    """
    Muestra las políticas actuales de contraseñas del sistema.
    Incluye longitud mínima, vencimiento, etc.
    """
    try:
        result = subprocess.run(["net", "accounts"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error al consultar la política de contraseñas: {e}"
