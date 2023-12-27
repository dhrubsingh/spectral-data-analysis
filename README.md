## Spectral Data Analysis API

# Astronomical Research Library

Package: [https://test.pypi.org/project/spectral-data-analysis-Tempestly18/](https://test.pypi.org/project/spectral-data-analysis-Tempestly18/)

## Overview

This library assists in astronomical research, focusing on classifying stars, galaxies, and QSOs. It interfaces with Sloan Digital Sky Survey (SDSS) services for spectral data access.

### Key Features

- **Data Preprocessing**: Normalization, outlier removal, interpolation, redshift correction.
- **Metadata Extraction**: Extracts various astronomical data fields.
- **Spectral Alignment**: Aligns wavelengths with interpolation.
- **Visualization**: Matplotlib-based spectral visualization.
- **Data Augmentation**: Derivative computations for spectra.
- **Additional Modules**: Cross-matching, machine learning classification, interactive visualization, spectral feature extraction.

## Installation

First, clone the repository and navigate to the project directory:

```bash
git clone git@github.com:dhrubsingh/spectral-data-analysis.git
cd spectral-data-analysis
pip install .
```

## Usage

### Basic Example

```python
from astronomical_research import StarGalaxyQSOClassifier
classifier = StarGalaxyQSOClassifier()
query = "SELECT * FROM sdss WHERE ..."
results = classifier.classify(query)
```

### Visualization Module

#### Overview
The Visualization module enables the plotting of spectrum data, providing a clear view of the Flux vs Wavelength relationship in astrophysical data.

#### Features
- Simple Data Visualization: Straightforward methods for spectrum data visualization.
- Data Extraction Integration: Fetch data using the DataExtraction class or from CSV files.
- Customizable Plots: Generate plots with gridlines and labels.

#### Usage

```python
from visualize_spectra import VisualizeSpectra
visualizer = VisualizeSpectra()
visualizer.get_spectrum_data(plate_id=1234, mjd=56789, fiberid=100)
visualizer.visualize()
```

## Documentation

Each module has its own documentation, containing instructions on how to use it. 

## License

Licensed under the MIT License. See `LICENSE` file.

## Acknowledgments

- Sloan Digital Sky Survey (SDSS)
