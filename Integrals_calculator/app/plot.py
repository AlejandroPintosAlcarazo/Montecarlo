import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, sin, log

def plot_function(func_str, x_range, filename):
    # Define the variable
    x = symbols('x')
    
    # Convert the function string to a symbolic expression
    func_expr = eval(func_str)
    
    # Convert the symbolic expression to a numerical function
    func = lambdify(x, func_expr, modules=['numpy'])

    # Generate x values
    x_vals = np.linspace(x_range[0], x_range[1], 400)
    y_vals = func(x_vals)

    # Plot the function
    plt.plot(x_vals, y_vals, label=f'{func_str}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Plot of {func_str}')
    plt.legend()
    plt.grid(True)

    # Fill the area between the function and the x-axis
    plt.fill_between(x_vals, y_vals, where=(x_vals >= x_range[0]) & (x_vals <= x_range[1]), color='blue', alpha=0.3)

    # Add vertical lines from the function to the x-axis at the range limits
    plt.vlines(x=x_range[0], ymin=0, ymax=func(x_range[0]), color='b', linestyle='--')
    plt.vlines(x=x_range[1], ymin=0, ymax=func(x_range[1]), color='b', linestyle='--')
    
    # Save the plot to a file
    plt.savefig(filename)
    plt.close()

