import matplotlib.pyplot as plt
import numpy as np

# Define the x-axis
x = np.linspace(0, 10, 500)

# Define functions for each plot
modulation_depth = np.sin(x) * np.exp(-0.1 * x)
phase_sweep = np.sin(x) * np.cos(2 * x)
peak_field = np.exp(-((x - 5) ** 2) / (2 * 0.8 ** 2))
log_decay = np.log1p(10 - x + 1)
gradient_domain = np.tanh(x - 5)

# Create plots
fig, axs = plt.subplots(5, 1, figsize=(8, 12), constrained_layout=True)

# Plot 1: Lattice Modulation Depth
axs[0].plot(x, modulation_depth, color="mediumblue")
axs[0].set_title("Lattice Modulation Depth Profile")
axs[0].set_ylabel("Amplitude")

# Plot 2: Phase Sweep Transition Map
axs[1].plot(x, phase_sweep, color="darkorange")
axs[1].set_title("Phase Sweep Transition Map")
axs[1].set_ylabel("Amplitude")

# Plot 3: Peak Field Density
axs[2].plot(x, peak_field, color="crimson")
axs[2].set_title("Peak Field Density")
axs[2].set_ylabel("Density")

# Plot 4: Log Decay H₃ Curve
axs[3].plot(x, log_decay, color="seagreen")
axs[3].set_title("Log Decay H₃ Curve")
axs[3].set_ylabel("Log Value")

# Plot 5: Gradient Domain Topology
axs[4].plot(x, gradient_domain, color="slategray")
axs[4].set_title("Gradient Domain Topology")
axs[4].set_xlabel("Position")
axs[4].set_ylabel("Gradient")

# Save the composite figure
output_path = "/mnt/data/QESR_Validation_Figure_Suite.png"
fig.suptitle("QESR Validation Figure Suite", fontsize=16)
plt.savefig(output_path)

output_path
