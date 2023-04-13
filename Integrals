# Import the "sympy" module for symbolic math
import sympy

# Create a symbol for x
x = sympy.symbols('x')

# Define the function f(x)
def f(x):
    return x**5/2 + 3*x

# Define the limits of the interval [a, b]
a, b = 0, 5

# Use the "integrate" function from the "sympy" module to find the indefinite integral of f(x)
F = sympy.integrate(f(x), x)

# Evaluate the indefinite integral at the limits of the interval [a, b] to find the definite integral
result = F.evalf(subs={x: b}) - F.evalf(subs={x: a})

# Print the result
print(result)
