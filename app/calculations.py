import numpy as np

def montecarlo_simulation(iterations=1000000):
    inside_circle = 0
    points = []

    for _ in range(iterations):
        x, y = np.random.uniform(-1, 1, 2)
        distance = x**2 + y**2
        points.append((x, y, distance <= 1))
        if distance <= 1:
            inside_circle += 1

    pi_estimate = (inside_circle / iterations) * 4
    return pi_estimate, points

