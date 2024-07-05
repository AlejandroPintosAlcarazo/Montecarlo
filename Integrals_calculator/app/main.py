from app.validate import validate_input
from app.plot import main_plot_function
from app.calculations import find_roots, find_domain

def main(function_str, a, b, iterations):
    is_valid = validate_input(function_str)
    if is_valid:
        print("La función es válida.")
        main_plot_function(function_str, a, b, iterations, 'output/function_plot.png')
        print("El gráfico se ha guardado como 'output/function_plot.png'.")

        domain = find_domain(function_str)
        print(f"Dominio: {domain}")

        roots = find_roots(function_str, a, b)
        print(f"Raíces numéricas: {roots}")
    else:
        print("La función no es válida.")
