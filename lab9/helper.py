import pandas as pd
import numpy as np

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Input Data (to be replaced with your measurements)
data = {
    "Level": [1, 2, 3, 4],  # Cylinder levels
    "Height (m)": [0.0, 0.0, 0.0, 0.0],  # Replace with your h_i in meters
    "Apparent Mass (kg)": [0.0, 0.0, 0.0, 0.0],  # Replace with your m_i in kg
}

# Create a DataFrame
df = pd.DataFrame(data)

# Measured Cylinder Dimensions
diameter = 0.02  # Replace with your d in meters (e.g., 2.00 cm = 0.02 m)
radius = diameter / 2

# Calculate Submerged Volume
df["Submerged Volume (m^3)"] = np.pi * radius**2 * df["Height (m)"]

# Buoyant Force
df["Buoyant Force (N)"] = df["Apparent Mass (kg)"] * g


# Results
print("Results:")
print("Submerged Volumes (m^3):", df["Submerged Volume (m^3)"].tolist())
print("Buoyant Forces (N):", df["Buoyant Force (N)"].tolist())

