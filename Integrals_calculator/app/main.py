from app.validate import validate_input
from app.plot import plot_function

def get_args():
    print("Calculadora de Integrales usando Monte Carlo")
    
    function_str = input("Introduce la función a integrar (usa 'x' como variable): ")
    a = float(input("Introduce el límite inferior del intervalo: "))
    b = float(input("Introduce el límite superior del intervalo: "))
    iterations = int(input("Introduce el número de iteraciones (puntos aleatorios): "))
    return function_str, a, b, iterations

def main():
    function_str, a, b, iterations = get_args()
    
    is_valid = validate_input(function_str)

    if is_valid:
        print("La función es válida.")
        plot_function(function_str, (a, b), 'function_plot.png')
        print("El gráfico se ha guardado como 'function_plot.png'.")
    else:
        print("La función no es válida.")

if __name__ == "__main__":
    main()

