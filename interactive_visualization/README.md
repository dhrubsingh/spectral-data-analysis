
## Interactive Visualization Module

### Overview
The Interactive Visualization module provides a dynamic and user-interactive way to visualize spectrum data in astrophysical research. It allows users to explore spectral data more intuitively through interactive features.

### Features
- **Interactive Plotting**: Visualizes spectrum data with interactive elements using matplotlib.
- **Zoom and Focus**: Users can select a rectangular region to zoom in on specific data points.
- **Dynamic Annotations**: Provides real-time wavelength and flux annotations when hovering over the plot.
- **Reset Functionality**: Allows users to reset the plot to its default view with the press of a key.

### Usage

#### Setting Up
Make sure `matplotlib`, `pandas`, `numpy`, and `mplcursors` are installed.

#### VisualizeSpectraInteractive Class
1. **Initialization**:
   ```python
   from visualize_spectra_interactive import VisualizeSpectraInteractive
   vs = VisualizeSpectraInteractive()
   ```

2. **Loading Data**:
   - Fetch spectrum data directly: `vs.get_spectrum_data(plate_id, mjd, fiberid)`
   - Load from a CSV file: `vs.get_data_from_csv(csv_file_path)`

3. **Visualization**:
   ```python
   vs.visualize_interactive()
   ```

### Example
```python
vs = VisualizeSpectraInteractive()
vs.get_spectrum_data(4055, 55359, 596)  # Fetch data
vs.visualize_interactive()  # Visualize data
```

### Integration
This module can be integrated with Data Processing and Data Augmentation modules for a comprehensive analysis workflow in astrophysical research.

### Conclusion
The Interactive Visualization module offers an advanced, user-friendly approach to exploring and analyzing spectrum data, enhancing the overall research experience in astrophysics.