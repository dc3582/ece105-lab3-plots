"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
import numpy as np


def generate_data(seed):
    """Generate synthetic temperature sensor data.
    
    Creates simulated temperature readings from two sensors over a 10-second
    interval with 200 samples each. Both sensors measure temperature in Celsius
    with realistic sensor noise.
    
    Parameters
    ----------
    seed : int
        Random seed for reproducibility. Controls the random number generator
        used to create sensor noise and baseline temperature variations.
    
    Returns
    -------
    sensor_a : ndarray
        Temperature readings from Sensor A in Celsius. Shape is (200,) with
        dtype float64.
    sensor_b : ndarray
        Temperature readings from Sensor B in Celsius. Shape is (200,) with
        dtype float64.
    timestamps : ndarray
        Time points in seconds from 0 to 10. Shape is (200,) with dtype float64.
    """
    rng = np.random.RandomState(seed)
    
    # Create timestamps from 0 to 10 seconds with 200 samples
    timestamps = np.linspace(0, 10, 200)
    
    # Generate baseline temperatures with realistic drifts
    sensor_a = 20 + 3 * np.sin(timestamps) + rng.normal(0, 0.5, 200)
    sensor_b = 22 + 2 * np.sin(timestamps + 0.5) + rng.normal(0, 0.5, 200)
    
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create scatter plot of sensor readings versus time.
    
    Plots temperature readings from two sensors as a function of time on the
    provided Axes object. Sensor A points are colored blue and Sensor B points
    are colored orange.
    
    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A in Celsius. Shape (n,).
    sensor_b : ndarray
        Temperature readings from Sensor B in Celsius. Shape (n,).
    timestamps : ndarray
        Time points in seconds. Shape (n,).
    ax : matplotlib.axes.Axes
        Axes object to modify in place. The scatter plot is drawn on this object.
    
    Returns
    -------
    None
        Modifies the Axes object in place without returning a value.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', s=50, alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', s=50, alpha=0.7)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Readings vs Time')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Create plot_histogram(sensor_a, sensor_b, timestamps, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_histogram(sensor_a, sensor_b, ax):
    """Create overlaid histogram of sensor temperature distributions.
    
    Plots overlapping histograms of temperature readings from two sensors with
    vertical dashed lines indicating each sensor's mean temperature. Uses 30 bins
    and semi-transparent colors so both distributions are visible.
    
    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A in Celsius. Shape (n,).
    sensor_b : ndarray
        Temperature readings from Sensor B in Celsius. Shape (n,).
    ax : matplotlib.axes.Axes
        Axes object to modify in place. The histogram is drawn on this object.
    
    Returns
    -------
    None
        Modifies the Axes object in place without returning a value.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A', color='blue')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B', color='orange')
    ax.axvline(np.mean(sensor_a), color='blue', linestyle='--', linewidth=2, 
               label=f'Sensor A mean: {np.mean(sensor_a):.2f}°C')
    ax.axvline(np.mean(sensor_b), color='orange', linestyle='--', linewidth=2,
               label=f'Sensor B mean: {np.mean(sensor_b):.2f}°C')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)

# Create plot_boxplot(sensor_a, sensor_b, timestamps, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.


def plot_boxplot(sensor_a, sensor_b, ax):
    """Create side-by-side box plot comparing sensor temperature distributions.
    
    Plots side-by-side box plots for temperature readings from two sensors with
    a horizontal dashed line indicating the overall mean of both sensors combined.
    
    Parameters
    ----------
    sensor_a : ndarray
        Temperature readings from Sensor A in Celsius. Shape (n,).
    sensor_b : ndarray
        Temperature readings from Sensor B in Celsius. Shape (n,).
    ax : matplotlib.axes.Axes
        Axes object to modify in place. The box plot is drawn on this object.
    
    Returns
    -------
    None
        Modifies the Axes object in place without returning a value.
    """
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=2, 
               label=f'Overall Mean: {overall_mean:.2f}°C')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Sensor Temperature Distribution Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.


def main():
    """Generate sensor data and create publication-quality visualizations.
    
    Creates synthetic temperature sensor data and produces three publication-quality
    plots (scatter, histogram, and box plot) saved as a PNG file. The plots are
    arranged in a 1x3 subplot grid and saved with tight bounding box at 150 DPI.
    
    Returns
    -------
    None
    """
    import matplotlib.pyplot as plt
    
    # Generate synthetic data with seed for reproducibility
    sensor_a, sensor_b, timestamps = generate_data(seed=42)
    
    # Create figure with 1x3 subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Create each plot on its corresponding axis
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    main()
