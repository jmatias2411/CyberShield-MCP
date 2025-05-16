# executors/base_executor.py

import subprocess
import json
from datetime import datetime
import os

class BaseExecutor:
    """
    Ejecuta herramientas o comandos locales desde el MCP.
    """

    def __init__(self, log_path: str = "data/acciones_log.csv"):
        os.makedirs("data", exist_ok=True)
        self.log_path = log_path

    def run_command(self, command: list[str], shell: bool = False) -> str:
        """
        Ejecuta un comando del sistema de forma segura y devuelve la salida.

        Args:
            command: Lista de strings (comando y argumentos).
            shell: Si True, ejecuta con shell (con precaución).

        Returns:
            str: Salida del comando o mensaje de error.
        """
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                shell=shell
            )
            output = result.stdout.strip() if result.returncode == 0 else result.stderr.strip()
            self._log_action("command", " ".join(command), result.returncode, output)
            return output
        except Exception as e:
            self._log_action("command", " ".join(command), -1, str(e))
            return f"❌ Error ejecutando comando: {e}"

    def _log_action(self, tipo: str, detalle: str, code: int, resultado: str):
        """
        Guarda en CSV un registro de acciones ejecutadas.
        """
        with open(self.log_path, "a", newline="", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()},{tipo},{detalle},{code},{json.dumps(resultado)}\n")
