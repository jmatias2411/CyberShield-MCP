# executors/docker_executor.py

import subprocess
from datetime import datetime
import json
import os

class DockerExecutor:
    """
    Ejecuta comandos dentro de contenedores Docker para herramientas MCP.
    """

    def __init__(self, container_name: str, log_path: str = "data/acciones_log.csv"):
        self.container_name = container_name
        os.makedirs("data", exist_ok=True)
        self.log_path = log_path

    def run(self, command: str) -> str:
        """
        Ejecuta un comando dentro del contenedor Docker especificado.

        Args:
            command (str): El comando a ejecutar dentro del contenedor.

        Returns:
            str: Resultado del comando o mensaje de error.
        """
        docker_cmd = ["docker", "exec", self.container_name, "bash", "-c", command]
        try:
            result = subprocess.run(docker_cmd, capture_output=True, text=True)
            salida = result.stdout.strip()
            error = result.stderr.strip()
            if result.returncode == 0:
                self._log_action("docker", command, 0, salida)
                return salida or "✅ Ejecutado (sin salida)"
            else:
                self._log_action("docker", command, result.returncode, error)
                return f"❌ Error: {error}"
        except Exception as e:
            self._log_action("docker", command, -1, str(e))
            return f"❌ Excepción al ejecutar en Docker: {e}"

    def _log_action(self, tipo: str, detalle: str, code: int, resultado: str):
        with open(self.log_path, "a", newline="", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()},{tipo},{detalle},{code},{json.dumps(resultado)}\n")
