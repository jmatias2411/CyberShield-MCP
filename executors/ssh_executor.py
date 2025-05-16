# executors/ssh_executor.py

import paramiko
from datetime import datetime
import os
import json

class SSHExecutor:
    def __init__(self, host: str, user: str, password: str, log_path: str = "data/acciones_log.csv"):
        self.host = host
        self.user = user
        self.password = password
        os.makedirs("data", exist_ok=True)
        self.log_path = log_path

    def run(self, command: str) -> str:
        """
        Ejecuta un comando en un servidor remoto vía SSH.
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.user, password=self.password)

            stdin, stdout, stderr = ssh.exec_command(command)
            salida = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            ssh.close()

            if error:
                self._log_action("ssh", command, 1, error)
                return f"❌ Error remoto: {error}"
            else:
                self._log_action("ssh", command, 0, salida)
                return salida or "✅ Comando ejecutado (sin salida)"
        except Exception as e:
            self._log_action("ssh", command, -1, str(e))
            return f"❌ Excepción SSH: {e}"

    def _log_action(self, tipo: str, detalle: str, code: int, resultado: str):
        with open(self.log_path, "a", newline="", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()},{tipo},{detalle},{code},{json.dumps(resultado)}\n")
