
# Visualization Module

## Overview
The Visualization module enables the plotting of spectrum data, allowing for a clear and detailed view of the Flux vs Wavelength relationship in astrophysical data.

## Features
- **Simple Data Visualization**: Offers straightforward methods for visualizing spectrum data.
- **Data Extraction Integration**: Seamlessly fetches data using the DataExtraction class or from CSV files.
- **Customizable Plots**: Generates customizable plots with gridlines and labels for better readability and analysis.

## Usage

### Setting Up
Ensure that `matplotlib` and `pandas` are installed, and the `data_extraction` module is available.

### VisualizeSpectra Class
1. **Initialization**:
   ```python
   from visualize_spectra import VisualizeSpectra
   visualizer = VisualizeSpectra()
   ```

2. **Loading Data**:
   - Fetch data directly: `visualizer.get_spectrum_data(plate_id, mjd, fiberid)`
   - Load from CSV file: `visualizer.get_data_from_csv(csv_file_path)`

3. **Visualization**:
   ```python
   visualizer.visualize()
   ```

## Example
```python
visualizer = VisualizeSpectra()
visualizer.get_spectrum_data(plate_id=1234, mjd=56789, fiberid=100)
visualizer.visualize()
```

## Integration
This module can be used in conjunction with Data Extraction and other analysis modules to provide a comprehensive view of spectrum data, aiding in astrophysical research.

## Conclusion
The Visualization module is an essential tool for effectively presenting spectrum data, enhancing the understanding and analysis of our astrophysical data.