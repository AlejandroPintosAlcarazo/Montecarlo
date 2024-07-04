# app/calculations.py
import numpy as np

def montecarlo_integration(f, a, b, iterations=10000):
    """
    Calcula la integral de una función f en el intervalo [a, b] utilizando el método de Monte Carlo.

    f: Función a integrar
    a: Límite inferior del intervalo
    b: Límite superior del intervalo
    iterations: Número de puntos aleatorios a generar
    """
    # Genera puntos aleatorios en el intervalo [a, b]
    x_random = np.random.uniform(a, b, iterations)
    
    # Evalúa la función en estos puntos
    f_values = f(x_random)
    
    # Calcula el promedio de los valores de la función
    mean_value = np.mean(f_values)
    
    # Calcula la integral como el promedio de los valores de la función multiplicado por la longitud del intervalo
    integral_value = (b - a) * mean_value
    
    return integral_value

