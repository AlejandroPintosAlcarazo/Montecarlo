import numpy as np
import sympy as sp
from scipy.optimize import fsolve

#esta funcion necesita un repaso, 
#esta lejos de estar bien ajustada, la distribucion uniforme es notablemente mejor
def generate_distribution(func_str, a, b, n):
    x = sp.symbols('x')
    func_expr = sp.sympify(func_str)
    func_derivative = sp.diff(func_expr, x)
    derivative_func = sp.lambdify(x, func_derivative, modules=['numpy'])
    x_vals = np.linspace(a, b, n)
    derivative_vals = np.abs(derivative_func(x_vals))
    prob_density = derivative_vals / np.sum(derivative_vals)
    points = np.random.choice(x_vals, size=n, p=prob_density)
    return points

def montecarlo_integration(f, a, b, iterations):
    x = sp.symbols('x')
    func_expr = sp.sympify(f)
    func = sp.lambdify(x, func_expr, modules=['numpy'])

    # Encontrar raíces en el intervalo [a, b]
    roots = find_roots(f, a, b)

    # Ordenar raíces y añadir los límites del intervalo
    roots = sorted([a] + roots + [b])

    integral_value = 0

    # Aplicar Monte Carlo en cada subintervalo
    for i in range(len(roots) - 1):
        
        #x_random = generate_distribution(f, roots[i], roots[i + 1], iterations)
        x_random = np.random.uniform(roots[i], roots[i + 1], iterations)
        f_values = func(x_random)
        mean_value = np.mean(f_values)
        sub_integral = (roots[i + 1] - roots[i]) * mean_value
        integral_value += sub_integral

    return integral_value

def find_roots(func_str, a, b, num_guesses=10):
    x = sp.symbols('x')
    func_expr = sp.sympify(func_str)
    func = sp.lambdify(x, func_expr, modules=['numpy'])

    def f_numeric(x):
        return func(x)

    initial_guesses = np.linspace(a, b, num_guesses)
    roots = []
    for guess in initial_guesses:
        try:
            root = fsolve(f_numeric, guess)
            root_value = f_numeric(root)
            # Comprobar si la raíz es válida, está dentro del intervalo y f(root) es cercano a 0
            if a <= root <= b and abs(root_value) < 1e-5 and not any(np.isclose(root, r, atol=1e-5) for r in roots):
                roots.append(root[0])
        except Exception as e:
            print(f"Error al encontrar la raíz en el punto inicial {guess}: {e}")
            continue
    return sorted(roots)

def find_domain(func_str):
    x = sp.symbols('x')
    func_expr = sp.sympify(func_str)
    domain = sp.calculus.util.continuous_domain(func_expr, x, sp.S.Reals)
    return domain
