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