#Compilación del código
FROM maven:3.8.5-openjdk-17 AS builder

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto (pom.xml y el código fuente)
COPY pom.xml .
COPY src ./src

# Compila el proyecto y genera el JAR
RUN mvn clean package -DskipTests

#Creación de la imagen final
FROM eclipse-temurin:17-jre-focal

# Establece el directorio de trabajo
WORKDIR /app

# Instalar cliente MySQL
RUN apt-get update && apt-get install -y default-mysql-client && rm -rf /var/lib/apt/lists/*

# Copia el JAR generado antes
COPY --from=builder /app/target/ArtistAPI-0.0.1-SNAPSHOT.jar app.jar

# Copia el script de espera al contenedor
COPY wait-for-mysql.sh /wait-for-mysql.sh
RUN chmod +x /wait-for-mysql.sh

# Expone la API en el puerto
EXPOSE 8080

# Comando para ejecutar la aplicación
ENTRYPOINT ["/wait-for-mysql.sh", "artist-db", "java", "-jar", "app.jar"]