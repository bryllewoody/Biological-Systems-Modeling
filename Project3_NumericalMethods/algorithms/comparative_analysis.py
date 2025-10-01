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
    steps = round(T / dt)  # Using round instead of int for accurate step count
    for _ in range(steps):
        N += k * N * dt
    return N

# --- Improved Euler Method ---
def improved_euler(N0, k, dt, T):
    N = N0
    steps = round(T / dt)  # Using round instead of int for accurate step count
    for _ in range(steps):
        d1 = k * N * dt
        N_pred = N + d1
        d2 = k * N_pred * dt
        N += 0.5 * (d1 + d2)
    return N

# --- RK4 Method ---
def rk4(N0, k, dt, T):
    N = N0
    steps = round(T / dt)  # Using round instead of int for accurate step count
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

print("\nNumerical Integration Comparison (dt = 0.1)")
print("-" * 75)
print(f"{'Time':>8}{'Analytical':>15}{'Euler':>15}{'Improved':>15}{'RK4':>15}")
print("-" * 75)

# Generate time points from 0 to 30 in steps of 0.1
t_data = []
for i in range(301):  # 0 to 300 (for 0.0 to 30.0)
    t_data.append(i * 0.1)

analytical_data = []
euler_data = []
improved_euler_data = []
rk4_data = []

for t in t_data:
    a = analytical(N0, k, t)
    e = euler(N0, k, dt_default, t)
    h = improved_euler(N0, k, dt_default, t)
    r = rk4(N0, k, dt_default, t)
    print(f"{t:8.1f}{a:15.6f}{e:15.6f}{h:15.6f}{r:15.6f}")
    
    analytical_data.append(a)
    euler_data.append(e)
    improved_euler_data.append(h)
    rk4_data.append(r)

# Save data to CSV
with open('exercise_5_5_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Time', 'Analytical', 'Euler', 'Improved Euler', 'RK4'])
    for i in range(len(t_data)):
        writer.writerow([t_data[i], analytical_data[i], euler_data[i], 
                        improved_euler_data[i], rk4_data[i]])

# Plot 1: Solution Comparison
plt.figure(figsize=(12, 6))
plt.plot(t_data, analytical_data, 'k-', label='Analytical', linewidth=2)
plt.plot(t_data, euler_data, 'b--', label='Euler')
plt.plot(t_data, improved_euler_data, 'g:', label='Improved Euler')
plt.plot(t_data, rk4_data, 'r-.', label='RK4')
plt.grid(False)
plt.xlabel('Time')
plt.ylabel('Population')
plt.title(f'Population Growth Comparison (dt={dt_default})')
plt.legend()
plt.savefig('exercise_5_5_comparison.png')
plt.close()

# Plot 2: Error Analysis
plt.figure(figsize=(12, 6))
euler_error = [e - a for e, a in zip(euler_data, analytical_data)]
improved_error = [h - a for h, a in zip(improved_euler_data, analytical_data)]
rk4_error = [r - a for r, a in zip(rk4_data, analytical_data)]

plt.plot(t_data, euler_error, 'b--', label='Euler Error')
plt.plot(t_data, improved_error, 'g:', label='Improved Euler Error')
plt.plot(t_data, rk4_error, 'r-.', label='RK4 Error')
plt.grid(False)
plt.xlabel('Time')
plt.ylabel('Error (Method - Analytical)')
plt.title(f'Error Analysis (dt={dt_default})')
plt.legend()
plt.savefig('exercise_5_5_errors.png')
plt.close()
