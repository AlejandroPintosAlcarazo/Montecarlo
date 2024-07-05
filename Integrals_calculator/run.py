import sys
from app.main import main

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python run.py <función> <límite_inferior> <límite_superior> <iteraciones>")
        sys.exit(1)

    function_str = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])
    iterations = int(sys.argv[4])

    main(function_str, a, b, iterations)
