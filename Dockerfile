# Dockerfile para CyberShield MCP con FastAPI
FROM python:3.11-slim

# Evita que Python genere archivos .pyc y usa UTF-8
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8

# Crear directorio de la app
WORKDIR /app

# Copiar archivos
COPY . /app

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install mcp[cli] fastapi uvicorn requests

# Exponer puerto para FastAPI
EXPOSE 4242

# Comando para arrancar FastAPI
CMD ["uvicorn", "fastapi_mcp_server:app", "--host", "0.0.0.0", "--port", "4242"]
