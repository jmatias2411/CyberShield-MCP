# tools/firewall.py
import subprocess

def block_port(port: int) -> str:
    cmd = ["netsh", "advfirewall", "firewall", "add", "rule",
           f"name=Block_Port_{port}", "dir=in", "action=block",
           "protocol=TCP", f"localport={port}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"Puerto {port} bloqueado."

def unblock_port(port: int) -> str:
    cmd = ["netsh", "advfirewall", "firewall", "delete", "rule", f"name=Block_Port_{port}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"Puerto {port} desbloqueado."

def block_ip(ip: str) -> str:
    cmd = ["netsh", "advfirewall", "firewall", "add", "rule",
           f"name=Block_IP_{ip}", "dir=in", "action=block",
           f"remoteip={ip}", "protocol=any"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"IP {ip} bloqueada."

def unblock_ip(ip: str) -> str:
    cmd = ["netsh", "advfirewall", "firewall", "delete", "rule", f"name=Block_IP_{ip}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or f"IP {ip} desbloqueada."

def list_firewall_rules() -> str:
    cmd = ["netsh", "advfirewall", "firewall", "show", "rule", "name=all"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or "No se encontraron reglas activas."