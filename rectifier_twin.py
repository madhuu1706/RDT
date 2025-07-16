import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# UI for input controls
st.title("Digital Twin – Full Wave Rectifier")
st.sidebar.header("Input Parameters")
voltage = st.sidebar.slider("Peak Voltage (V)", 1, 20, 10)
frequency = st.sidebar.slider("Frequency (Hz)", 10, 100, 50)

# Generate time and waveforms
t = np.linspace(0, 1 / frequency, 1000)
Vin = voltage * np.sin(2 * np.pi * frequency * t)
Vout = np.abs(Vin)

# Plotting
fig, ax = plt.subplots()
ax.plot(t, Vin, label='Input AC')
ax.plot(t, Vout, label='Output DC', linestyle='--')
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title("Rectifier Simulation")
ax.legend()
ax.grid(True)

st.pyplot(fig)
