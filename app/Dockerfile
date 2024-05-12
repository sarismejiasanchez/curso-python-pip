# Usa una imagen base de Python
FROM python:3.10.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos para instalar las dependencias
COPY requirements.txt /app/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia todo el contenido actual en el directorio de trabajo (/app) al contenedor
COPY . .

# Define el comando que se ejecutará cuando se inicie el contenedor
CMD ["python3", "main.py"]