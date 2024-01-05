import matplotlib.pyplot as plt
import numpy as np

def plot_signals(x, y_array, y_lines=[], y_names=[], title="Plot of Signals", log_x=False, log_y=False, xlabel="X-axis", ylabel="Y-axis", save=False, filename="plot.png"):
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

    # Add vertical lines
    for y_line in y_lines:
        ax.axvline(x=y_line, color='magenta', linestyle='--')


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

def plot_signals_side_by_side(x, y1, y2, y_names1=[], y_names2=[], title1="", title2="", log_x=False, log_y=False, xlabel="X-axis", ylabel="Y-axis", save=False, filename="plot.png", sharey=True):
    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Set log scale for x-axis if log_x is True
    if log_x:
        ax1.set_xscale("log")
        ax2.set_xscale("log")

    # Set log scale for y-axis if log_y is True
    if log_y:
        ax1.set_yscale("log")
        ax2.set_yscale("log")

    # Plot each signal in the array for the first graph
    for i, signal in enumerate(y1):
        if y_names1:
            label = y_names1[i]
        else:
            label = f"Signal {i + 1}"
        ax1.plot(x, signal, label=label)

    # Plot each signal in the array for the second graph
    for i, signal in enumerate(y2):
        if y_names2:
            label = y_names2[i]
        else:
            label = f"Signal {i + 1}"
        ax2.plot(x, signal, label=label)

    # Add labels
    ax1.set_xlabel(xlabel + (" (log scale)" if log_x else ""))
    ax1.set_ylabel(ylabel + (" (log scale)" if log_y else ""))
    ax2.set_xlabel(xlabel + (" (log scale)" if log_x else ""))
    ax2.set_ylabel(ylabel + (" (log scale)" if log_y else ""))

    # Set title
    ax1.set_title(title1)
    ax2.set_title(title2)

    # Add legend
    ax1.legend()
    ax2.legend()

    # Adjust layout for better spacing
    plt.tight_layout()

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

def generate_random_numbers(n, range_start, range_end, min_distance):
    numbers = []

    for _ in range(n):
        new_number = np.random.randint(range_start, range_end)
        while any(abs(new_number - num) < min_distance for num in numbers):
            new_number = np.random.randint(range_start, range_end)
        numbers.append(new_number)

    return numbers