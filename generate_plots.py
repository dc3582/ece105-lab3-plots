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
