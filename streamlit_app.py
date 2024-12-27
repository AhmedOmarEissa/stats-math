import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_t_distribution(degrees_of_freedom, num_samples):
    """
    Generates a t-distribution by dividing a standard normal distribution 
    by the square root of a chi-squared distribution.

    Args:
        degrees_of_freedom: Degrees of freedom for the t-distribution.
        num_samples: Number of samples to generate.

    Returns:
        A NumPy array containing the generated t-distribution samples.
    """
    # Generate standard normal samples
    z_samples = np.random.standard_normal(num_samples)

    # Generate chi-squared samples
    chi_squared_samples = np.random.chisquare(degrees_of_freedom, num_samples)

    # Calculate t-distribution samples
    t_samples = z_samples / np.sqrt(chi_squared_samples / degrees_of_freedom)

    return t_samples

# Streamlit App Title
st.title("T-Distribution Generator")

# Sidebar inputs
degrees_freedom = st.sidebar.slider("Degrees of Freedom", min_value=1, max_value=30, value=10, step=1)
num_samples = st.sidebar.number_input("Number of Samples", min_value=100, max_value=10000, value=1000, step=100)

# Generate t-distribution samples
if st.sidebar.button("Generate T-Distribution"):
    t_distribution_samples = generate_t_distribution(degrees_freedom, num_samples)

    # Display results
    st.write(f"Generated {num_samples} samples with {degrees_freedom} degrees of freedom.")

    # Plot the distribution
    fig, ax = plt.subplots()
    ax.hist(t_distribution_samples, bins=30, density=True, alpha=0.7, color="blue")
    ax.set_title("T-Distribution Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Density")
    st.pyplot(fig)

    # Display statistics
    mean = np.mean(t_distribution_samples)
    std_dev = np.std(t_distribution_samples)
    st.write(f"Mean: {mean:.4f}")
    st.write(f"Standard Deviation: {std_dev:.4f}")
