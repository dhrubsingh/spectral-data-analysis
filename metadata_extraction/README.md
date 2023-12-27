
# Metadata Extraction Module

## Overview
The Metadata Extraction module is designed to extract and process metadata from the SDSS (Sloan Digital Sky Survey) Database, aiding in astrophysical research by providing crucial information about astronomical objects.

## Features
- **Database Querying**: Facilitates querying the SDSS database and retrieving data in a structured format.
- **CSV File Reading**: Allows reading data from local CSV files.
- **Data Column Extraction**: Provides functionality to extract specific columns from the data, useful for extracting identifiers, redshifts, etc.
- **Coordinate and Identifier Extraction**: Specialized functions to extract object identifiers and coordinates.

## Usage

### Setting Up
Ensure `pandas`, `requests`, and `urllib.parse` are available in your environment.

### DataExtraction Class
1. **Initialization**:
   ```python
   from metadata_extraction import DataExtraction
   extractor = DataExtraction()
   ```

2. **Querying Database**:
   ```python
   query = 'SELECT * FROM YourTable WHERE YourConditions'
   extractor.query_database(query)
   ```

3. **Reading CSV File**:
   ```python
   extractor.read_csv_file(csv_file_path)
   ```

4. **Extracting Specific Columns or Identifiers**:
   - For specific columns: `extractor.get_cols(['col1', 'col2'])`
   - For identifiers: `extractor.get_identifiers()`
   - For coordinates: `extractor.get_coordinates()`

## Example
```python
extractor = DataExtraction()
extractor.query_database('SELECT objid, ra, dec FROM SpecObj WHERE plate=4055')
coordinates = extractor.get_coordinates()
```

## Integration
This module can be seamlessly integrated with other data processing and analysis modules in the toolkit, providing essential metadata for comprehensive astrophysical studies.

## Conclusion
The Metadata Extraction module is a vital tool for accessing and manipulating metadata from astronomical databases, playing a key role in the analysis and interpretation of astrophysical data.