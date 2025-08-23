# Dockerfile
FROM python:3.11-slim

# Criar diretório de trabalho
WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código para o container
COPY . .

# Expõe a porta que o FastAPI vai usar
EXPOSE 8001

# Comando de inicialização (entrypoint)
CMD ["uvicorn", "github_agent_endpoint:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
