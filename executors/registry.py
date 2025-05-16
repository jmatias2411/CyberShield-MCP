# executors/registry.py

import importlib
import os

TOOLS_PATH = "tools"

def listar_tools_disponibles():
    """
    Lista todos los scripts en la carpeta tools/ que definen una función main().
    """
    disponibles = []
    for archivo in os.listdir(TOOLS_PATH):
        if archivo.endswith(".py") and not archivo.startswith("__"):
            nombre_modulo = archivo[:-3]
            try:
                modulo = importlib.import_module(f"{TOOLS_PATH}.{nombre_modulo}")
                if hasattr(modulo, "main"):
                    disponibles.append(nombre_modulo)
            except Exception:
                pass  # Ignorar módulos que fallan al importar
    return disponibles


def ejecutar_tool(tool_name: str, params: dict = None) -> str:
    """
    Ejecuta una herramienta del directorio tools por su nombre si define main().
    """
    try:
        modulo = importlib.import_module(f"{TOOLS_PATH}.{tool_name}")
        if hasattr(modulo, "main"):
            return modulo.main(params or {})
        else:
            return f"⚠️ La herramienta '{tool_name}' no define una función main()."
    except ModuleNotFoundError:
        return f"❌ Herramienta '{tool_name}' no encontrada."
    except Exception as e:
        return f"❌ Error al ejecutar '{tool_name}': {e}"
