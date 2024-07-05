# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al directorio de trabajo
COPY . .

# Asegúrate de que el directorio output exista
RUN mkdir -p /app/output

# Especifica el comando por defecto para ejecutar cuando se inicia el contenedor
CMD ["python", "run.py"]
