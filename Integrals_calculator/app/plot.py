import numpy as np
import os
import matplotlib.pyplot as plt
import sympy as sp
from app.calculations import find_roots, montecarlo_integration

def plot_function(func_str, x_range, filename, integral_value, subintervals):
    # Definir la variable
    x = sp.symbols('x')
    
    # Convertir la cadena de texto a una expresión de SymPy
    func_expr = sp.sympify(func_str)
    
    # Convertir la expresión de SymPy a una función numérica
    func = sp.lambdify(x, func_expr, modules=['numpy'])

    # Generar valores de x
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = func(x_vals)

    # Graficar la función
    plt.plot(x_vals, y_vals, label=f'{func_str}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    # Crear el título en formato LaTeX
    integral_title = f'Integral: $\\int_{{{x_range[0]}}}^{{{x_range[1]}}} ({func_str}) \\, dx = {integral_value:.4f}$'
    plt.title(integral_title, fontsize=12)
    
    plt.legend()
    plt.grid(True)

    # Rellenar el área entre la función y el eje x
    plt.fill_between(x_vals, y_vals, where=(x_vals >= x_range[0]) & (x_vals <= x_range[1]), color='blue', alpha=0.3)

    # Añadir líneas verticales desde la función hasta el eje x en los límites del rango
    plt.vlines(x=x_range[0], ymin=0, ymax=func(x_range[0]), color='b', linestyle='--')
    plt.vlines(x=x_range[1], ymin=0, ymax=func(x_range[1]), color='b', linestyle='--')
    
    # Dibujar los subintervalos y sus integrales
    for i, (start, end, sub_integral) in enumerate(subintervals):
        mid = (start + end) / 2
        plt.vlines(x=start, ymin=0, ymax=func(start), color='g', linestyle='--')
        plt.vlines(x=end, ymin=0, ymax=func(end), color='g', linestyle='--')
        plt.text(mid, func(mid) / 2, f'{sub_integral:.4f}', horizontalalignment='center', color='black')

    # Guardar el gráfico en un archivo
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    plt.close()

def main_plot_function(func_str, a, b, iterations, filename):
    # Encontrar raíces numéricas
    roots = find_roots(func_str, a, b)
    roots = sorted([a] + roots + [b])

    integral_value = 0
    subintervals = []

    # Calcular la integral usando Monte Carlo en cada subintervalo
    for i in range(len(roots) - 1):
        start = roots[i]
        end = roots[i + 1]
        sub_integral = montecarlo_integration(func_str, start, end, iterations)
        subintervals.append((start, end, sub_integral))
        integral_value += sub_integral

    # Graficar la función con los intervalos y la integral total
    plot_function(func_str, (a, b), filename, integral_value, subintervals)
