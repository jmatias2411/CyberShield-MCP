import paramiko

def ejecutar_remoto(ip, user, password, comando):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=user, password=password)
        stdin, stdout, stderr = ssh.exec_command(comando)
        return stdout.read().decode() or stderr.read().decode()
    except Exception as e:
        return f"Error SSH: {e}"
