import numpy as np
import sympy as sp
from scipy.optimize import fsolve

def montecarlo_integration(f, a, b, iterations=10000):
    # Definir la variable simbólica
    x = sp.symbols('x')
    
    # Convertir la cadena de texto a una expresión de SymPy
    func_expr = sp.sympify(f)
    
    # Convertir la expresión de SymPy a una función numérica
    func = sp.lambdify(x, func_expr, modules=['numpy'])

    def f_numeric(x):
        return func(x)

    # Encontrar raíces en el intervalo [a, b] usando scipy.optimize.fsolve
    initial_guesses = np.linspace(a, b, 10)
    roots = []
    for guess in initial_guesses:
        root = fsolve(f_numeric, guess)
        if a <= root <= b and not any(np.isclose(root, r, atol=1e-5) for r in roots):
            roots.append(root[0])

    # Ordenar raíces y añadir los límites del intervalo
    roots = sorted([a] + roots + [b])

    integral_value = 0

    # Aplicar Monte Carlo en cada subintervalo
    for i in range(len(roots) - 1):
        x_random = np.random.uniform(roots[i], roots[i + 1], iterations)
        f_values = func(x_random)
        mean_value = np.mean(f_values)
        sub_integral = (roots[i + 1] - roots[i]) * mean_value
        integral_value += sub_integral

    return integral_value

def find_roots_scipy(func_str, a, b):
    x = sp.symbols('x')
    func_expr = sp.sympify(func_str)
    func = sp.lambdify(x, func_expr, modules=['numpy'])

    def f_numeric(x):
        return func(x)

    initial_guesses = np.linspace(a, b, 10)
    roots = []
    for guess in initial_guesses:
        root = fsolve(f_numeric, guess)
        if a <= root <= b and not any(np.isclose(root, r, atol=1e-5) for r in roots):
            roots.append(root[0])
    return sorted(roots)

def find_domain(func_str):
    x = sp.symbols('x')
    func_expr = sp.sympify(func_str)
    domain = sp.calculus.util.continuous_domain(func_expr, x, sp.S.Reals)
    return domain

