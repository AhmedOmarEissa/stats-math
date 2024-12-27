import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def generate_t_distribution(degrees_of_freedom, num_points):
    """
    Generates a t-distribution by dividing a standard normal distribution 
    by the square root of a chi-squared distribution.

    Args:
        degrees_of_freedom: Degrees of freedom for the t-distribution.
        num_points: Number of points to generate.

    Returns:
        A NumPy array containing the generated t-distribution points.
    """
    # Generate standard normal points
    z_points = np.random.standard_normal(num_points)

    # Generate chi-squared points
    chi_squared_points = np.random.chisquare(degrees_of_freedom, num_points)

    # Calculate t-distribution points
    t_points = z_points / np.sqrt(chi_squared_points / degrees_of_freedom)

    return z_points, t_points ,chi_squared_points

# Streamlit App Title
st.title("t-Distribution Generator ")

# Sidebar inputs
degrees_freedom = st.sidebar.slider("Degrees of Freedom", min_value=1, max_value=50, value=10, step=1)
num_points = st.sidebar.number_input("Number of points", min_value=100, max_value=10000, value=1000, step=100)

# Generate t-distribution points
# if st.sidebar.button("Generate t-Distribution"):
z_distribution, t_distribution_points , chi_squared_points = generate_t_distribution(degrees_freedom, num_points)

# Display results
st.write(f"Generated {num_points} points with {degrees_freedom} degrees of freedom.")

# Plot the distribution using a KDE chart
fig, ax = plt.subplots()
sns.kdeplot(z_distribution, ax=ax, fill=False, color="red", alpha=0.7,label = 'z_distribution')
sns.kdeplot(t_distribution_points, ax=ax, fill=False, color="blue", alpha=0.7,label = 't_distribution')
# sns.kdeplot(chi_squared_points, ax=ax, fill=False, color="black", alpha=0.7,label = 'z_distribution')

ax.legend()

ax.set_title("t-Distribution Vs z-Distribution ")
ax.set_xlabel("Value")
ax.set_ylabel("Density")
ax.set_xlim(-5,5)
st.pyplot(fig)


# Display statistics
mean = np.mean(t_distribution_points)
std_dev = np.std(t_distribution_points)
z_mean = np.mean(z_distribution)
z_std_dev = np.std(z_distribution)

st.write(f"t-Mean: {mean:.4f} , t-Standard Deviation: {std_dev:.4f}")
st.write(f"z-Mean: {z_mean:.4f} , z-Standard Deviation: {z_std_dev:.4f} ")
