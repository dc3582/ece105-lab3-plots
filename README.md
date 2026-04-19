# Sensor Data Visualization Generator

Generate publication-quality temperature sensor data visualizations from synthetic measurements.

## Installation

1. Activate the `ece105` conda environment:
   ```bash
   conda activate ece105
   ```

2. Install dependencies using conda or mamba:
   ```bash
   conda install numpy matplotlib
   ```
   
   Or with mamba:
   ```bash
   mamba install numpy matplotlib
   ```

## Usage

Run the script to generate sensor data and create visualizations:

```bash
python generate_plots.py
```

This will create synthetic temperature readings from two sensors and produce a publication-quality figure with three subplots.

## Example Output

The script generates `sensor_analysis.png`, a figure containing three plots:

1. **Scatter Plot** (left): Temperature readings from both sensors plotted against time (0-10 seconds). Sensor A is shown in blue, Sensor B in orange. Visualizes the temporal evolution of sensor readings.

2. **Histogram** (center): Overlaid distribution of temperature readings from both sensors using 30 bins with semi-transparent colors. Vertical dashed lines indicate each sensor's mean temperature, allowing comparison of measurement distributions.

3. **Box Plot** (right): Side-by-side box plots comparing the quartile ranges and median values for both sensors. A red dashed line marks the combined mean temperature across both sensors.

All plots include appropriate axis labels with units, titles, legends, and grids for clarity.

## AI Tools Used and Disclosure

[Placeholder: Describe any AI tools used in developing this script and provide appropriate attribution or disclosure as required by your institution.]