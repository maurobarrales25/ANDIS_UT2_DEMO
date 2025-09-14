FROM python:3.12
#Crear directorio de trabajo
WORKDIR /app
#Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#Copiar todo el proyecto
COPY . .
COPY start.sh /start.sh
RUN chmod +x /start.sh
#Comando por defecto para correr FastAPI
CMD ["/start.sh"]