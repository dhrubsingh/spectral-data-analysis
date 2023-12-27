
# Wavelength Alignment Module

## Overview
The Wavelength Alignment module is designed to align spectral data within a specified wavelength range, enhancing the consistency and comparability of spectrum data in astrophysical research.

## Features
- **Data Alignment**: Aligns the wavelength of spectrum data to a specified range.
- **Integration with Data Extraction**: Works in conjunction with the DataExtraction class to fetch and process spectrum data.
- **Customizable Range**: Allows users to set their own minimum and maximum wavelengths for alignment.

## Usage

### Setting Up
Ensure `pandas` and the `data_extraction` module are available.

### WavelengthAlign Class
1. **Initialization**:
   ```python
   from wavelength_align import WavelengthAlign
   aligner = WavelengthAlign()
   ```

2. **Loading Data**:
   ```python
   aligner.get_spectrum_data(plate_id, mjd, fiberid)
   ```

3. **Aligning Data**:
   ```python
   aligned_data = aligner.align_data(min_wavelength, max_wavelength)
   ```

## Example
```python
aligner = WavelengthAlign()
aligner.get_spectrum_data(plate_id=1234, mjd=56789, fiberid=100)
aligned_data = aligner.align_data(3800, 7500)
```

## Integration
This module can be integrated with other data processing and visualization modules to facilitate comprehensive astrophysical data analysis.

## Conclusion
Wavelength Alignment is a vital tool in standardizing spectrum data, crucial for accurate and consistent astrophysical research.