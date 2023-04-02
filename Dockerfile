# Usa la imagen oficial de Python como imagen base
FROM python:3.9-slim-buster

# Define un directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY app.py .
COPY templates templates
COPY static static
COPY model.h5 .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080
EXPOSE 8080

# Inicia la aplicación Flask
CMD ["python", "app.py"]
