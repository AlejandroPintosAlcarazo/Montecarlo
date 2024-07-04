#!/bin/bash

# Construir la imagen Docker
docker build -t montecarlo_simulation .

# Ejecutar el contenedor
docker run --name montecarlo_simulation_container montecarlo_simulation

# Copiar el archivo desde el contenedor al host
docker cp montecarlo_simulation_container:/app/montecarlo_simulation.png .

# Detener y eliminar el contenedor
docker rm montecarlo_simulation_container

