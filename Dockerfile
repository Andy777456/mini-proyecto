FROM python:3.11

# Establece variables de entorno para Python.
# PYTHONDONTWRITEBYTECODE=1: Evita que Python escriba archivos .pyc en el contenedor.
# PYTHONUNBUFFERED=1: Fuerza que la salida de Python se envíe directamente al terminal (stdout/stderr) sin búfer.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Actualiza la lista de paquetes e instala 'git'.
# 'git' es necesario porque el Dockerfile clona el repositorio.
RUN apt-get update && apt-get install -y git

# Establece el directorio de trabajo dentro del contenedor.
# Todos los comandos subsiguientes se ejecutarán desde /app.
WORKDIR /app

# Copia el contenido del directorio actual del host (donde está el Dockerfile) al directorio de trabajo /app en el contenedor.
COPY . .

# Ejecuta una serie de comandos en el shell del contenedor.
# rm -rf /app/*: Elimina el contenido copiado previamente para asegurar una copia limpia del repositorio.
# git clone ...: Clona el repositorio de GitHub en el directorio /app.
# pip install -r requirements.txt: Instala todas las dependencias de Python listadas en requirements.txt.
# python manage.py migrate: Aplica las migraciones de la base de datos de Django.
# python manage.py runserver 0.0.0.0:8000: Inicia el servidor de desarrollo de Django, accesible desde cualquier IP en el puerto 8000.
CMD sh -c "\
    rm -rf /app/* && \
    git clone https://github.com/Andy777456/mini-proyecto.git /app && \
    pip install -r requirements.txt && \
    python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000 \
"
