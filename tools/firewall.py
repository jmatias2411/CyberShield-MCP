# tools/firewall.py

import subprocess

def block_port(port: int) -> str:
    """Bloquea un puerto TCP en el firewall de Windows"""
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name=Block_Port_{port}", "dir=in", "action=block",
        "protocol=TCP", f"localport={port}"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"Puerto {port} bloqueado."

def block_ip(ip: str) -> str:
    """Bloquea una IP remota en el firewall de Windows"""
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name=Block_IP_{ip}", "dir=in", "action=block",
        f"remoteip={ip}", "protocol=any"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"IP {ip} bloqueada."
