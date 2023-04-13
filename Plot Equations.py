import matplotlib.pyplot as plt
import sympy
from sympy.functions import sin, cos

# Create a symbol for x
x = sympy.symbols('x')

# Define the function f(x)
def f(x):
    return sin(x) + cos(x)


# Define the limits of the interval [a, b]
a, b = 0, 5

# Use the "integrate" function from the "sympy" module to find the indefinite integral of f(x)
F = sympy.integrate(f(x), x)

# Evaluate the indefinite integral at the limits of the interval [a, b] to find the definite integral
result = F.evalf(subs={x: b}) - F.evalf(subs={x: a})


# Plot the function f(x)
sympy.plot(f(x))

# show the plot
plt.show()
