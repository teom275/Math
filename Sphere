import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define radius of the sphere
r = 1

# Define number of points to use for plotting the sphere
n = 100

# Generate x, y, and z coordinates of points on a sphere
u = np.linspace(0, 2 * np.pi, n)
v = np.linspace(0, np.pi, n)
x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the sphere
ax.plot_surface(x, y, z, color='b')

# Show the plot
plt.show()
