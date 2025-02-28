# Waves
# Quantum and Classical Wave Equation Solvers

This repository provides Python implementations for solving the time-dependent Schrödinger equation and a classical wave equation, both using finite difference methods. Inspiration for the quantum solver comes from **Welch Labs**' YouTube series on the Schrödinger equation. A `Math.pdf` document is included to detail the equations behind these models.

---

## Contents

1. [Overview](#overview)  
2. [Mathematical Documentation](#mathematical-documentation)  
3. [Modules](#modules)  
   - [Schrodinger_Equation.py](#schrodinger_equationpy)  
   - [Wave_Equation.py](#wave_equationpy)  
4. [Acknowledgments](#acknowledgments)  
5. [License](#license)

---

## Overview

The main focus of this repository is to demonstrate numerical methods for wave-like phenomena in both quantum (Schrödinger) and classical (wave) contexts:

- **Schrödinger_Equation.py** implements the time-dependent Schrödinger equation using a finite difference approach for the spatial discretization and explicit time-stepping.  
- **Wave_Equation.py** provides a simple finite difference solver for the classical wave equation in one dimension.

Both scripts can be adapted or extended with different boundary/initial conditions, damping terms, and higher-dimensional domains.

---

## Mathematical Documentation

- **Math.pdf**  
  This document provides a detailed overview of the wave and Schrödinger equations. Most of the information here was found on Wikipedia.

---

## Modules

### Schrodinger_Equation.py
- Implements a **finite difference** method (with explicit time stepping) to solve the time-dependent Schrödinger equation.
- Demonstrates how to set initial wave packets and evolve them under free or potential-influenced scenarios.
- Code structure inspired by the **Welch Labs** series on the Schrödinger equation, adapted into Python for visualization and experimentation.

### Wave_Equation.py
- Implements a **finite difference** solver for the 1D classical wave equation.
- Includes basic initial conditions and boundary conditions for demonstration.
- Can be easily modified to incorporate damping, variable propagation speed, or more complex geometries.

---

## Acknowledgments

- **Welch Labs (YouTube)**: Provided inspiration for the Schrödinger equation.

---

## License

Open-source
