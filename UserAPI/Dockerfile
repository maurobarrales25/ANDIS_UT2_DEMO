FROM python:3.12
#Crear directorio de trabajo
WORKDIR /app
#Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#Copiar todo el proyecto
COPY . .
#Comando por defecto para correr FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
