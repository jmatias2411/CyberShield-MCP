# utils/commands.py

import subprocess

def run_command(command: list[str], shell: bool = False) -> str:
    """
    Ejecuta un comando del sistema de forma segura y devuelve la salida.
    
    Args:
        command: Lista de strings representando el comando y sus argumentos.
        shell: Si True, ejecuta con el shell del sistema. Úsalo con precaución.

    Returns:
        str: Salida estándar del comando, o mensaje de error si falla.
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=shell
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error [{result.returncode}]: {result.stderr.strip()}"
    except FileNotFoundError:
        return f"Comando no encontrado: {command[0]}"
    except Exception as e:
        return f"Excepción al ejecutar el comando: {e}"
