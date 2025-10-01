import math
import numpy as np
import matplotlib.pyplot as plt
import csv

# --- Parameters ---
N0 = 10.0     # Initial population
k = 0.10      # Growth rate
dt_default = 0.1
T_end = 30.0

# --- Analytical Solution ---
def analytical(N0, k, t):
    return N0 * math.exp(k * t)

# --- Euler Method ---
def euler(N0, k, dt, T):
    N = N0
    steps = int(T / dt)
    for _ in range(steps):
        N += k * N * dt
    return N

# --- RK4 Method ---
def rk4(N0, k, dt, T):
    N = N0
    steps = int(T / dt)
    for _ in range(steps):
        D1 = k * N * dt
        N1 = N + 0.5 * D1
        D2 = k * N1 * dt
        N2 = N + 0.5 * D2
        D3 = k * N2 * dt
        N3 = N + D3
        D4 = k * N3 * dt
        N += (D1 + 2*D2 + 2*D3 + D4) / 6.0
    return N

# --- Exercise 5-6: Finding optimal time step for Euler method ---
# Goal: Find largest dt where Euler matches RK4 to 5 decimal places at t=20

print("\n=== Exercise 5-6 ===")
# Calculate reference solution using RK4 with default time step
T_target = 20.0  # Target time point for comparison
rk4_val = rk4(N0, k, dt_default, T_target)  # Reference value from RK4
rk4_5dp = round(rk4_val, 5)  # Rounded to 5 decimal places for comparison

# Print header and column labels
print(f"RK4 reference value at t={T_target}: {rk4_val:.10f}")
print("\nComparison of Euler method with different time steps:")
print("-" * 75)
print(f"{'dt':>12}{'Euler Value':>20}{'Error from RK4':>20}{'Match?':>12}")
print("-" * 75)

# Generate decreasing time steps for testing
# Using 50 points between 1e-6 and 1e-8, in reverse order (large to small)
dt_values = np.linspace(1e-8, 1e-6, num=50)[::-1]
results = []  # Store results for plotting and CSV output
max_matching_dt = None  # Will store largest dt that matches RK4 to 5dp

for dt in dt_values:
    val = euler(N0, k, dt, T_target)
    error = val - rk4_val
    matches = round(val, 5) == rk4_5dp
    
    # Print each comparison with aligned columns
    print(f"{dt:12.2e}{val:20.10f}{error:20.2e}{('Yes' if matches else 'No'):>12}")
    
    results.append({
        'dt': dt,
        'euler_value': val,
        'error': error,
        'matches': matches
    })
    if matches and max_matching_dt is None:
        max_matching_dt = dt
