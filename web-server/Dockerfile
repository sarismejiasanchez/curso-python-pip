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

# Etablece que el contenedor ejecute un servidor Uvicorn, sirviendo la aplicación web definida en main.py en el puerto 80 y disponible para conexiones externas.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]