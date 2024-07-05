#!/bin/bash

# Nombre de la imagen Docker
IMAGE_NAME="montecarlo_simulation"

# Nombre del contenedor Docker
CONTAINER_NAME="montecarlo_simulation_container"

# Verificar si se han pasado suficientes argumentos
if [ "$#" -ne 4 ]; then
    echo "Uso: $0 <función> <límite_inferior> <límite_superior> <iteraciones>"
    exit 1
fi

# Construir la imagen Docker
echo "Construyendo la imagen Docker..."
docker build -t $IMAGE_NAME .

# Verificar si la imagen se construyó correctamente
if [ $? -eq 0 ]; then
    echo "Imagen Docker construida con éxito."

    # Eliminar cualquier contenedor existente con el mismo nombre
    echo "Eliminando cualquier contenedor existente con el nombre $CONTAINER_NAME..."
    docker rm -f $CONTAINER_NAME 2>/dev/null || true

    # Ejecutar el contenedor Docker con los argumentos pasados
    echo "Ejecutando el contenedor Docker..."
    docker run --name $CONTAINER_NAME $IMAGE_NAME python run.py "$1" "$2" "$3" "$4"

    # Verificar si el contenedor se está ejecutando
    if [ $? -eq 0 ]; then
        echo "Contenedor Docker ejecutándose con éxito."
        echo "Copiando la imagen generada al host..."

        # Asegúrate de que el directorio output exista en el host
        mkdir -p output

        # Copiar la imagen generada al host
        docker cp $CONTAINER_NAME:/app/output/function_plot.png ./output/

        if [ $? -eq 0 ]; then
            echo "Imagen copiada con éxito a la carpeta 'output' del host."
        else
            echo "Error al copiar la imagen desde el contenedor al host."
        fi

        # Detener y eliminar el contenedor
        echo "Deteniendo y eliminando el contenedor Docker..."
        docker rm -f $CONTAINER_NAME
    else
        echo "Error al ejecutar el contenedor Docker."
    fi
else
    echo "Error al construir la imagen Docker."
fi
