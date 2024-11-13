import pandas as pd

# Redefining the data with clear placeholders based on user feedback

# Theoretical Calculation Section
theoretical_data = {
    "Parameter": ["Disk Diameter, D", "Disk Mass, M", "Radius, R = D / 2", "I_theo", "delta I_theo"],
    "Value": ["[Input]", "[Input]", "[Calculated]", "[Calculated]", "[Calculated]"],
    "Uncertainty": ["[Input]", "[Input]", "[Calculated]", "", ""],
    "Notes": [
        "Measured with calipers",
        "Measured with scale",
        "R = D / 2",
        "Formula from textbook",
        "Error propagation"
    ]
}

# Experimental Data - Cylinder and Friction Mass Section
experimental_data = {
    "Parameter": ["Cylinder Diameter, d", "Radius, r = d / 2", "Friction Mass, m_friction"],
    "Value": ["[Input]", "[Calculated]", "[Input]"],
    "Uncertainty": ["[Input]", "[Calculated]", "[Input]"],
    "Notes": [
        "Measured with calipers",
        "r = d / 2",
        "Measured with scale"
    ]
}

# Trial Data for 6 sets of 5 trials each and an average row
trial_data = {
    "Set #": ["Set 1"]*6 + ["Set 2"]*6 + ["Set 3"]*6 + ["Set 4"]*6 + ["Set 5"]*6 + ["Set 6"]*6,
    "Trial #": ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5", "Set Avg"] * 6,
    "Hanging Mass (m_hanging)": ["[Input] ± [Input]"] * 36,
    "Linear Acceleration (a)": ["[Input]"] * 36,
    "Angular Acceleration (alpha)": ["alpha = a / r"] * 36,
    "Torque (tau)": ["tau = r * m * (g - a)"] * 36
}

# Plot Data Section for Tau vs Alpha values from the experiment
plot_data = {
    "Set #": [f"Set {i+1}" for i in range(6)],
    "Average Torque (tau)": ["[Calculated]"] * 6,
    "Angular Acceleration (alpha)": ["[Calculated]"] * 6,
    "Uncertainty in Tau (delta tau)": ["[Calculated]"] * 6
}

# Final Comparison Section
comparison_data = {
    "Parameter": ["Moment of Inertia, I"],
    "Theoretical": ["I_theo ± delta I_theo"],
    "Experimental": ["I_exp ± delta I_exp"],
    "Difference": ["[Calculated]"],
    "Agreement": ["[Yes/No]"]
}

# Convert dictionaries into dataframes
df_theoretical = pd.DataFrame(theoretical_data)
df_experimental = pd.DataFrame(experimental_data)
df_trials = pd.DataFrame(trial_data)
df_plot = pd.DataFrame(plot_data)
df_comparison = pd.DataFrame(comparison_data)

# Write data to .ods file
file_path = "Moment_of_Inertia_Lab_Updated.ods"
with pd.ExcelWriter(file_path, engine="odf") as writer:
    df_theoretical.to_excel(writer, sheet_name="Theoretical Calculation", index=False)
    df_experimental.to_excel(writer, sheet_name="Experimental Data", index=False)
    df_trials.to_excel(writer, sheet_name="Trial Data", index=False)
    df_plot.to_excel(writer, sheet_name="Plot Data", index=False)
    df_comparison.to_excel(writer, sheet_name="Final Comparison", index=False)

file_path