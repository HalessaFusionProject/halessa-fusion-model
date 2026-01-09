import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Simulation parameters for the QESR nano lattice sweep
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# Simulate a quantum-electronic spin resonance lattice field
def qesr_field(x, y):
    r = np.sqrt(x**2 + y**2)
    return np.sin(3 * r) * np.exp(-0.1 * r)

Z = qesr_field(X, Y)

# Plotting the lattice field resonance pattern
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
ax.set_title('QESR Nano Lattice Sweep: Resonance Field Topography')
ax.set_xlabel('X Position (nm)')
ax.set_ylabel('Y Position (nm)')
ax.set_zlabel('Field Intensity')

plt.tight_layout()
plt.show()
