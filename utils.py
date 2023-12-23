import matplotlib.pyplot as plt
import numpy as np

def plot_signals(x, y_array, y_names=[], title="Plot of Signals", log_x=False, log_y=False, xlabel="X-axis", ylabel="Y-axis", save=False, filename="plot.png"):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set log scale for x-axis if log_x is True
    if log_x:
        ax.set_xscale("log")

    # Set log scale for y-axis if log_y is True
    if log_y:
        ax.set_yscale("log")

    # Plot each signal in the array
    for i, signal in enumerate(y_array):
        if y_names:
            label = y_names[i]
        else:
            label = f"Signal {i + 1}"
        ax.plot(x, signal, label=label)

    # Set title
    ax.set_title(title)

    # Add labels
    ax.set_xlabel(xlabel + (" (log scale)" if log_x else ""))
    ax.set_ylabel(ylabel + (" (log scale)" if log_y else ""))

    # Add legend
    ax.legend()

    # Save the plot if save is True
    if save:
        plt.savefig(filename)

    # Display the plot
    plt.show()

def generate_noisy_polynomial(degree, noise_level, num_points):
    # Generate random polynomial coefficients
    coefficients = np.random.randn(degree + 2)

    # Generate x values
    x_values = np.linspace(-1, 1, num_points)

    # Calculate polynomial values
    y_values = np.polyval(coefficients, x_values)

    # Add noise to the y values
    noisy_y_values = y_values + noise_level * np.random.randn(num_points)

    return x_values, noisy_y_values, coefficients