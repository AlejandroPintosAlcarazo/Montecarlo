#!/bin/bash

# Verificar si se han pasado suficientes argumentos
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <iteraciones>"
    exit 1
fi

ITERATIONS=$1

# Construir la imagen Docker
echo "Construyendo la imagen Docker..."
docker build -t montecarlo_simulation .

# Verificar si la imagen se construyó correctamente
if [ $? -eq 0 ]; then
    echo "Imagen Docker construida con éxito."

    # Eliminar cualquier contenedor existente con el mismo nombre
    echo "Eliminando cualquier contenedor existente con el nombre montecarlo_simulation_container..."
    docker rm -f montecarlo_simulation_container 2>/dev/null || true

    # Ejecutar el contenedor Docker con los argumentos pasados
    echo "Ejecutando el contenedor Docker..."
    docker run --name montecarlo_simulation_container montecarlo_simulation python run.py $ITERATIONS

    # Verificar si el contenedor se ejecutó correctamente
    if [ $? -eq 0 ]; then
        echo "Contenedor Docker ejecutándose con éxito."
        echo "Copiando la imagen generada al host..."

        # Asegúrate de que el directorio output exista en el host
        mkdir -p output

        # Copiar la imagen generada al host
        docker cp montecarlo_simulation_container:/app/output/function_plot.png ./output/

        if [ $? -eq 0 ]; then
            echo "Imagen copiada con éxito a la carpeta 'output' del host."
        else
            echo "Error al copiar la imagen desde el contenedor al host."
        fi

        # Detener y eliminar el contenedor
        echo "Deteniendo y eliminando el contenedor Docker..."
        docker rm -f montecarlo_simulation_container
    else
        echo "Error al ejecutar el contenedor Docker."
    fi
else
    echo "Error al construir la imagen Docker."
fi
