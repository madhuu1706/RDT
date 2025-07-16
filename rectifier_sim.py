import numpy as np
import matplotlib.pyplot as plt

# Time vector for 1 cycle of 50Hz
t = np.linspace(0, 0.04, 1000)

# Input AC signal (10V peak)
Vin = 10 * np.sin(2 * np.pi * 50 * t)

# Full-wave rectified output
Vout = np.abs(Vin)

# Plotting
plt.figure(figsize=(10,5))
plt.plot(t, Vin, label='Input AC (Vin)')
plt.plot(t, Vout, label='Output DC (Vout)', linestyle='--')
plt.title("Full-Wave Rectifier Output")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid(True)
plt.show()
