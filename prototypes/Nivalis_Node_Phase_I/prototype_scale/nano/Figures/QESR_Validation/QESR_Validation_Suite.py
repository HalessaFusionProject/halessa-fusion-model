# Retry once more due to transient client error from previous attempts

import matplotlib.pyplot as plt
import numpy as np

# Create mock data for each QESR validation figure
x = np.linspace(0, 10, 500)
mod_depth = np.sin(x) * np.exp(-0.1 * x)
phase_sweep = np.sin(x) * np.cos(2 * x)
peak_density = np.exp(-((x - 5) ** 2) / 2)
log_decay = np.log1p(10 - x + 1)
gradient_domain = np.tanh(x - 5)

# Create subplots
fig, axs = plt.subplots(5, 1, figsize=(8, 20))
fig.suptitle("QESR Validation Figure Suite", fontsize=16)

# Plot each figure
axs[0].plot(x, mod_depth, label='Mod Depth Profile', color='dodgerblue')
axs[0].set_title('Fig 1: Lattice Modulation Depth Profile')
axs[0].set_ylabel('Mod Depth')

axs[1].plot(x, phase_sweep, label='Phase Sweep Map', color='orchid')
axs[1].set_title('Fig 2: Phase Sweep Transition Map')
axs[1].set_ylabel('Transition Value')

axs[2].plot(x, peak_density, label='Peak Field Density', color='goldenrod')
axs[2].set_title('Fig 3: Peak Field Density')
axs[2].set_ylabel('Density')

axs[3].plot(x, log_decay, label='H3 Log Decay', color='darkgreen')
axs[3].set_title('Fig 4: Log Decay H₃ Curve')
axs[3].set_ylabel('Log Decay')

axs[4].plot(x, gradient_domain, label='Gradient Topology', color='indigo')
axs[4].set_title('Fig 5: Gradient Domain Topology')
axs[4].set_ylabel('Normalized Gradient')
axs[4].set_xlabel('Domain Axis')

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.97])

# Save the plot to a file
output_path = "/mnt/data/QESR_Validation_Composite_Figure.png"
plt.savefig(output_path)
output_path

