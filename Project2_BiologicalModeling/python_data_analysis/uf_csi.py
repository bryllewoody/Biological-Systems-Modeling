import math
import numpy as np
import matplotlib.pyplot as plt

# Parameters
T0 = 37          # initial body temp (°C)
C = 8            # environmental temp (°C)
k = 0.06         # cooling constant (per hour)
T_measured = 19  # measured body temp (°C)
found_time = 8   # found at 8 am Sunday

# Solve for time since death
t_since_death = -(1/k) * math.log((T_measured - C) / (T0 - C))

print(f"Estimated time since death: {t_since_death:.2f} hours")

# Generate cooling curve (0–48 hours)
time_hours = np.linspace(0, 48, 200)
T = C + (T0 - C) * np.exp(-k * time_hours)

# Plot
plt.figure(figsize=(8,5))
plt.plot(time_hours, T, label="Cooling Curve", linewidth=2)
plt.axhline(y=T_measured, color='r', linestyle='--', label=f"Measured Temp {T_measured}°C")
plt.axvline(x=t_since_death, color='g', linestyle='--',
            label=f"Time of death ≈ {t_since_death:.1f}h before discovery")
plt.xlabel("Time since death (hours)")
plt.ylabel("Body Temperature (°C)")
plt.title("Newton's Law of Cooling: Body Temperature Over Time")
plt.legend()

# Save to file
plt.savefig("cooling_48h_case.png", dpi=300, bbox_inches="tight")