import matplotlib.pyplot as plt
import pandas as pd
from data_extraction.data_extraction import DataExtraction

class WavelengthAlign:
    def __init__(self):
        self.data = None

    def get_spectrum_data(self, plate_id, mjd, fiberid):
        data_extractor = DataExtraction(plate_id, mjd, fiberid)
        data_extractor.get_spectrum_data()  # This will fetch and store data in data_extractor
        self.data = data_extractor.data     # Assign the fetched data to self.data

    def align_data(self, min_wavelength, max_wavelength):
        if self.data is not None:
            # get current min and max
            curr_min, curr_max = self.data['Wavelength'].min(), self.data['Wavelength'].max()
       
            # scale accordingly
            scale = ((self.data['Wavelength'] - curr_min) * (max_wavelength - min_wavelength)) / (curr_max - curr_min) + min_wavelength
            self.data['Aligned_Wavelength'] = scale
            return self.data
        else:
            print("Data is not available. Please fetch the data first.")
            return None

