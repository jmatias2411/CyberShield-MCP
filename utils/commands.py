# utils/commands.py

import subprocess
import importlib
import sys
import os
import csv
import json
from datetime import datetime

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
            return f"❌ Error [{result.returncode}]: {result.stderr.strip()}"
    except FileNotFoundError:
        return f"❌ Comando no encontrado: {command[0]}"
    except Exception as e:
        return f"❌ Excepción al ejecutar el comando: {e}"


def ejecutar_tool(tool_name: str, params: dict = None) -> str:
    """
    Importa dinámicamente una herramienta desde tools/ y ejecuta su función main().
    También registra la acción en un log CSV.

    Args:
        tool_name: Nombre del módulo dentro de tools/ (sin .py).
        params: Diccionario con parámetros opcionales para la función main().

    Returns:
        str: Resultado devuelto por la herramienta, o mensaje de error.
    """
    try:
        modulo = importlib.import_module(f"tools.{tool_name}")
        if hasattr(modulo, "main"):
            resultado = modulo.main(params or {})
            registrar_accion(tool_name, params or {})
            return resultado
        else:
            return f"⚠️ La herramienta '{tool_name}' no define una función main()."
    except ModuleNotFoundError:
        return f"❌ Herramienta '{tool_name}' no encontrada en tools/"
    except Exception as e:
        return f"❌ Error ejecutando '{tool_name}': {e}"


def registrar_accion(tool_name: str, params: dict):
    """
    Guarda en CSV una entrada de ejecución de herramienta con su timestamp.

    Args:
        tool_name: Nombre de la herramienta ejecutada.
        params: Parámetros usados.
    """
    os.makedirs("data", exist_ok=True)
    log_path = "data/acciones_log.csv"
    with open(log_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            tool_name,
            json.dumps(params, ensure_ascii=False)
        ])
