import sys
from app.main import main

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python run.py <iteraciones>")
        sys.exit(1)

    iterations = int(sys.argv[1])

    main(iterations)
