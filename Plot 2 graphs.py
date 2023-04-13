# Import the necessary libraries
import matplotlib.pyplot as plt
import numpy as np  # Import numpy for the sin and cos functions
import math # Import math Library

# Define the equations you want to plot
def f(x):
    return np.sin(np.pi*(x+1/2))  # Use the sin function from numpy

def g(x):
    return np.cos(np.pi*(x))  # Use the cos function from numpy

# Generate data for the x-axis
x = np.linspace(0, 10, 1000)

# Calculate the y-values for each equation using the x-values
y1 = f(x)
y2 = g(x)

# Create the plot
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")

# Add a legend and show the plot
plt.legend()
plt.show()
