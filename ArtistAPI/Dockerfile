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

# Copia el JAR generado antes
COPY --from=builder /app/target/ArtistAPI-0.0.1-SNAPSHOT.jar app.jar

# Expone la API en el puerto
EXPOSE 8080

# Comando para ejecutar la aplicación
ENTRYPOINT ["java", "-jar", "app.jar"]