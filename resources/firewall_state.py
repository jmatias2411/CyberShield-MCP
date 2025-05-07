# resources/firewall_state.py

import subprocess

def get_firewall_rules() -> str:
    """
    Devuelve todas las reglas activas del firewall de Windows.
    Usa netsh para extraer la info en formato de texto.
    """
    try:
        result = subprocess.run(
            ["netsh", "advfirewall", "firewall", "show", "rule", "name=all"],
            capture_output=True,
            text=True
        )
        return result.stdout or "No se encontraron reglas activas."
    except Exception as e:
        return f"Error al obtener reglas del firewall: {e}"
