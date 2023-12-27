
# Data Preprocessing Module

## Overview
The Data Preprocessing module is essential for preparing spectral data for analysis in astrophysical research. It includes functionalities for redshift correction, normalization, outlier removal, and interpolation.

## Features
- **Redshift Correction**: Adjusts wavelengths based on redshift values to compute Emit Wavelength.
- **Normalization**: Standardizes the wavelength and flux data for consistent analysis.
- **Outlier Removal**: Removes statistical outliers from the data.
- **Interpolation**: Interpolates flux values for given wavelengths.

## Usage

### Setting Up
Ensure `scipy`, `sklearn`, `pandas`, and `data_extraction` module are installed.

### PreProcessing Class
1. **Initialization**:
   ```python
   from data_preprocessing import PreProcessing
   preprocessor = PreProcessing(plateid, mjd, fiberid)
   ```

2. **Redshift Correction**:
   ```python
   preprocessor.redshift_correction()
   ```

3. **Normalization**:
   ```python
   preprocessor.normalization()
   ```

4. **Outlier Removal**:
   ```python
   preprocessor.outlier_removal()
   ```

5. **Interpolation**:
   ```python
   interpolated_data = preprocessor.interpolation(wavelengths)
   ```

## Example
```python
preprocessor = PreProcessing(plateid=4055, mjd=55359, fiberid=596)
preprocessor.redshift_correction()
preprocessor.normalization()
preprocessor.outlier_removal()
wavelengths = [4000, 4500, 5000]
interpolated_data = preprocessor.interpolation(wavelengths)
```

## Integration
This module integrates seamlessly with other modules like Data Extraction, Data Augmentation, and Visualization for a comprehensive astrophysical data analysis workflow.

## Conclusion
Data Preprocessing is a crucial step in the analysis of astrophysical data, ensuring data quality and reliability for subsequent analysis stages.