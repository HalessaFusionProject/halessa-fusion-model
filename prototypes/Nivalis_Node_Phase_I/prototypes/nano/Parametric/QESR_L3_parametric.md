# QESR Layer 3 – Nodal Inversion Junction (Parametric Form)

The following functions define a harmonic inversion surface suitable for rendering the QESR Layer 3 lattice:

**Parametric equations:**

x(u, v) = (1 + 0.3 * sin(5 * v)) * cos(u)  
y(u, v) = (1 + 0.3 * sin(5 * v)) * sin(u)  
z(u, v) = sin(v) + 0.1 * sin(3 * u)

**Parameter ranges:**

- u ∈ [0, 2π]  
- v ∈ [−π, π]

**Key Features:**

- **Rotational symmetry**: Maintained through the `(cos(u), sin(u))` shell.  
- **Nodal gating**: Modulated via `sin(5 * v)` and `sin(3 * u)` to generate multi-phase interference.  
- **Harmonic elevation**: `z(u, v)` provides standing-wave bulging via vertical sinusoid.  
- **Compression nodes**: Expressed as inward dips at `v = ±π/2` due to constructive resonance minima.

This surface represents the **QESR inversion bridge** — a dynamic harmonic junction in the 5-layer fusion scaffold, ideal for visualization via Hyperspace’s parametric renderer.