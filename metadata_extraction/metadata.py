import pandas as pd
from urllib.parse import quote
import requests
from csv import reader
from io import StringIO
from data_extraction.data_extraction import DataExtraction

"""Class to facilitate metadata extraction"""
class MetadataExtraction:

    """Initializing data to be read in/stored from SDSS Database"""
    def __init__(self, plateid, mjd, fiberid):
        self.data_extraction = DataExtraction(plateid, mjd, fiberid)
        self.data = self.data_extraction.get_metadata()
        
    """Function to extract certain columns from the data, which can be used by the user to extract identifiers, redshifts, etc"""
    def get_cols(self, col_names):
        if (self.data is not None) and all(col in self.data.columns for col in col_names): return self.data[col_names]
        else: raise Exception(f"Error: Check that data is not None and has columns {col_names}")
    
    """Function to extract identifiers from data"""
    def get_identifiers(self):
        return self.get_cols(['specObjID'])

    """Function to extract coordinates from data"""
    def get_coordinates(self):
        return self.get_cols(['ra', 'dec'])

    """Function to extract final redshift and redshift error from data"""
    def get_redshift(self):
        return self.get_cols(['z', 'zErr'])

    """Function to extract class from data"""
    def get_class(self):
        return self.get_cols(['class'])