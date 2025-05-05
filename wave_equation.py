import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Wave Model | Finite Difference Method

# -----------------------------------------
# Simulation Parameters
# -----------------------------------------

# Mesh
Lx = np.pi
Nx = 100
dx = Lx / Nx
x = np.linspace(0, Lx, Nx)  # from 0 to Lx, with Nx points

# Constants
c = 2.0

# Time Step CFL Condition
buffer = 0.5  # for CFL condition to ensure stability

dt = dx / c * buffer
print(f"Time Step: {dt}")


Nt = 1000

# -----------------------------------------
# Initialize Scalar Fields
# -----------------------------------------

# ICs
phi_old = np.ones_like(x) * np.sin(x * 5)  # phi field matches the x mesh with phi = 1 at each point
velocity_ic = -c * np.gradient(phi_old, dx) / 2
# velocity_ic = 8

# determine phi from velocity IC
phi = phi_old + dt * velocity_ic

# phi_new_2[1:-1] = 2 * phi_new_1[1:-1] - phi[1:-1] + (dt * c) ** 2 * (phi[2:] + phi[:-2] - 2 * phi[1:-1]) / (dx ** 2)

# -----------------------------------------
# Algorithm
# -----------------------------------------


def wave():

    global phi_old, phi

    phi_new = phi.copy()

    # Solving for phi_new with forward difference for time (arrays are same size despite shifts)

    phi_new[1:-1] = (2 * phi[1:-1] - phi_old[1:-1] + (dt * c) ** 2 *
                     (phi[2:] + phi[:-2] - 2 * phi[1:-1]) / (dx ** 2))

    phi_old[:] = phi
    phi[:] = phi_new

    return phi


# -----------------------------------------
# Visuals
# -----------------------------------------

fig, ax = plt.subplots(figsize=(12, 8), constrained_layout=True)

font_size = 10

# Advection
phi_line, = ax.plot(x, phi)
ax.set_xlim(0, Lx)
ax.set_ylim(-5, 5)
ax.set_xlabel('Position (m)', fontsize=14)
ax.set_ylabel('Phi', fontsize=14)
ax.set_title('1D Wave Simulation', fontsize=16)


def animate(frame):
    global phi

    phi = wave()
    phi_line.set_ydata(phi)
    ax.set_title(f'1D Wave Simulation', fontsize=16)

    return phi_line


# Create the animation object
anim = FuncAnimation(fig, animate, frames=Nt, interval=50, blit=False)

# Display the animation
plt.show()
