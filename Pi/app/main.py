import matplotlib.pyplot as plt
import os
from app.calculations import montecarlo_simulation

def main(iterations):
    # Realiza la simulación
    pi_estimate, points = montecarlo_simulation(iterations)

    # Separa los puntos dentro y fuera del círculo
    inside_x = [x for x, y, inside in points if inside]
    inside_y = [y for x, y, inside in points if inside]
    outside_x = [x for x, y, inside in points if not inside]
    outside_y = [y for x, y, inside in points if not inside]

    # Configura el gráfico
    plt.figure(figsize=(6,6))
    plt.scatter(inside_x, inside_y, color='blue', alpha=0.5, label='Inside Circle')
    plt.scatter(outside_x, outside_y, color='red', alpha=0.5, label='Outside Circle')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title(f'Simulación de Montecarlo - Estimación de Pi: {pi_estimate:.4f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')

    # Asegúrate de que el directorio output exista
    os.makedirs('output', exist_ok=True)

    # Guarda el gráfico en un archivo
    plt.savefig('output/function_plot.png')
    print(f"Gráfico guardado como 'output/function_plot.png' con una estimación de Pi: {pi_estimate:.4f}")

if __name__ == "__main__":
    main()

