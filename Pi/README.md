# Estimating π Using Monte Carlo Method

## Overview

This example demonstrates how to estimate the value of π using the Monte Carlo Method. By randomly sampling points within a square and counting how many fall inside a quarter circle, we can approximate π.

## Method

1. **Generate Random Points**: Randomly distribute points within a unit square.
2. **Count Points Inside the Circle**: Determine how many points fall inside the quarter circle.
3. **Estimate π**: Use the ratio of points inside the circle to the total number of points to estimate π.

## Why This Formula Works

The formula to estimate π is derived from the geometric properties of a circle. By randomly generating points within a unit square and counting how many fall inside a quarter circle, we can use the ratio of points inside the circle to the total number of points to estimate π. The ratio of the area of the quarter circle to the area of the unit square is π/4. Therefore, the estimate of π can be calculated as:

\[ \text{pi\_estimate} = \left(\frac{\text{inside\_circle}}{\text{iterations}}\right) \times 4 \]

This formula works because the unit circle has a radius of 1, and the area of a full circle is π, making the area of a quarter circle π/4. By multiplying the ratio by 4, we obtain an estimate for π.

## Results

Below is a visual representation of the Monte Carlo simulation for estimating π:

![Monte Carlo Simulation Demo](../assets/Pi_plot.png)

## Usage

To run the Monte Carlo simulation for estimating π, follow these steps:

### Using Python

Ensure you have Python and the required libraries installed. Then, run the simulation with the desired number of iterations:

python run.py <iterations>

### Using Docker
Ensure Docker is installed on your system. Navigate to the Pi directory in your terminal and run the simulation using the provided shell script:
./run.sh <iterations>
