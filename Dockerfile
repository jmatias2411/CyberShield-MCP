# Dockerfile para CyberShield MCP con FastAPI
FROM python:3.11-slim

# ─── Configuración del entorno ─────────────────────────────────
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8

# ─── Crear carpeta de la app ───────────────────────────────────
WORKDIR /app

# ─── Copiar archivos de la app ─────────────────────────────────
COPY . /app

# ─── Instalar dependencias ─────────────────────────────────────
# Si tienes requirements.txt, úsalo; si no, instala dependencias comunes
RUN apt-get update && apt-get install -y gcc && \
    pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; else \
    pip install "fastapi[all]" uvicorn paramiko psutil requests; fi

# ─── Crear carpeta de datos ────────────────────────────────────
RUN mkdir -p /app/data

# ─── Exponer puerto por defecto ────────────────────────────────
EXPOSE 4242

# ─── Comando de arranque ───────────────────────────────────────
CMD ["uvicorn", "fastapi_mcp_server:app", "--host", "0.0.0.0", "--port", "4242"]
