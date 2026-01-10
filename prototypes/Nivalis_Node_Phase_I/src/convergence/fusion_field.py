import numpy as np

def psi(x, y, z, t, A=1.0, kx=2*np.pi, ky=2*np.pi, omega=1.0, alpha=1.0):
    return A * np.sin(kx * x + omega * t) * np.cos(ky * y - omega * t) * np.exp(-alpha * z**2)

def phi(x, y, t, beta=0.1, N=5):
    theta = np.arctan2(y, x)
    return sum(np.sin(n * theta) * np.exp(-n * beta * t) for n in range(1, N+1))

def rho_default(x, t):
    return 1.0 + 0.05 * np.sin(2 * np.pi * x - 0.5 * t)

def Q_total(x, y, z, t, sigma=1.0, rho_func=rho_default):
    rho = rho_func(x, t)
    return sigma * rho * phi(x, y, t) * psi(x, y, z, t)
