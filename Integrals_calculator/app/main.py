from app.validate import validate_input

def main():
    print("Calculadora de Integrales usando Monte Carlo")
    
    function_str = input("Introduce la función a integrar (usa 'x' como variable): ")
    a = float(input("Introduce el límite inferior del intervalo: "))
    b = float(input("Introduce el límite superior del intervalo: "))
    iterations = int(input("Introduce el número de iteraciones (puntos aleatorios): "))

    is_valid = validate_input(function_str)

    if is_valid:
        print("La función es válida.")
    else:
        print("La función no es válida.")

if __name__ == "__main__":
    main()

