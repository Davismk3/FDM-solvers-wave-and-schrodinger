import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Schrodinger Model | Finite Difference Method

# -----------------------------------------
# Simulation Parameters
# -----------------------------------------

# Mesh
Lx = np.pi
Nx = 100
dx = Lx / Nx
x = np.linspace(0, Lx, Nx)  # from 0 to Lx, with Nx points

# Constants
h = 1.0
m = 1.0

# Time Step CFL Condition
buffer = 0.01  # for CFL condition to ensure stability

dt = (dx * 2 * m) / h * buffer
print(f"Time Step: {dt}")


Nt = 1000

# -----------------------------------------
# Initialize Scalar Fields
# -----------------------------------------

# Gaussian Initial Condition (Avoids Instability)
x0 = Lx / 2 + Lx / 3  # Center of the wave packet
sigma = 0.2  # Width of the wave packet
k0 = - 10.0  # Initial momentum

x1 = Lx / 2 - Lx / 3
k1 = - k0

phi_R = (
    np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.cos(k0 * x) +
    np.exp(-((x - x1) ** 2) / (2 * sigma ** 2)) * np.cos(k1 * x)
)
phi_I = (
    np.exp(-((x - x0) ** 2) / (2 * sigma ** 2)) * np.sin(k0 * x) +
    np.exp(-((x - x1) ** 2) / (2 * sigma ** 2)) * np.sin(k1 * x)
)

"""phi_R = np.ones_like(x) * 0.0
phi_I = np.ones_like(x) * 0.0
phi_R[30:-30] = 1.0"""

probability_density = phi_R ** 2 + phi_I ** 2


# -----------------------------------------
# Algorithm
# -----------------------------------------


def wavefunctions():

    global phi_R, phi_I, probability_density

    # Real wavefunction
    phi_R_new = phi_R.copy()

    R_laplace = (phi_I[2:] + phi_I[:-2] - 2 * phi_I[1:-1]) / (dx ** 2)
    R_coefficient = - h / (2 * m)
    phi_R_new[1:-1] = phi_R[1:-1] + dt * R_coefficient * R_laplace

    # BCs
    phi_R[0] = 0.0  # Dirichlet
    phi_R[-1] = 0.0  # Dirichlet

    phi_R[:] = phi_R_new

    # Imaginary wavefunction
    phi_I_new = phi_I.copy()

    I_laplace = (phi_R[2:] + phi_R[:-2] - 2 * phi_R[1:-1]) / (dx ** 2)
    I_coefficient = h / (2 * m)
    phi_I_new[1:-1] = phi_I[1:-1] + dt * I_coefficient * I_laplace

    # BCs
    phi_I[0] = phi_I[1]  # Dirichlet
    phi_I[-1] = 0.0  # Dirichlet

    phi_I[:] = phi_I_new

    probability_density = phi_R ** 2 + phi_I ** 2


    return phi_R, phi_I, probability_density


# -----------------------------------------
# Visuals
# -----------------------------------------

fig, ax = plt.subplots(figsize=(12, 8), constrained_layout=True)

font_size = 10

# Advection
probability_density_line, = ax.plot(x, probability_density)
ax.set_xlim(0, Lx)
ax.set_ylim(0, 10)
ax.set_xlabel('Position (m)', fontsize=14)
ax.set_ylabel('|Ψ|² (Probability Density)', fontsize=14)
ax.set_title('1D Quantum Wave Simulation', fontsize=16)


def animate(frame):
    global phi_R, phi_I, probability_density

    phi_R, phi_I, probability_density = wavefunctions()
    probability_density_line.set_ydata(probability_density)
    ax.set_title(f'1D Quantum Wave Simulation', fontsize=16)

    integrate = sum(probability_density)
    print(integrate)

    return probability_density_line


# Create the animation object
anim = FuncAnimation(fig, animate, frames=Nt, interval=50, blit=False)

# Display the animation
plt.show()
