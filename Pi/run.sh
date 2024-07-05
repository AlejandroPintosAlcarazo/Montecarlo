#!/bin/bash

# Construir la imagen Docker
docker build -t montecarlo_simulation .

# Ejecutar el contenedor
docker run --name montecarlo_simulation_container montecarlo_simulation

# Copiar el archivo desde el contenedor al host
docker cp montecarlo_simulation_container:/app/output/function_plot.png ./output/

# Verificar si la copia fue exitosa
if [ $? -eq 0 ]; then
    echo "Imagen copiada con éxito a la carpeta 'output' del host."
else
    echo "Error al copiar la imagen desde el contenedor al host."
fi

# Detener y eliminar el contenedor
docker rm montecarlo_simulation_container
