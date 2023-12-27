import matplotlib.pyplot as plt
import pandas as pd
from data_extraction.data_extraction import DataExtraction

class VisualizeSpectra:
    def __init__(self):
        self.data = None

    def get_spectrum_data(self, plate_id, mjd, fiberid):
        data_extractor = DataExtraction(plate_id, mjd, fiberid)
        self.data = data_extractor.get_spectrum_data()

    def get_data_from_csv(self, csv_file_path):
        self.data = pd.read_csv(csv_file_path)
  
    def visualize(self):
        plt.plot(self.data['Wavelength'], self.data['Flux'])
        plt.grid(True)
        plt.xlabel('Wavelength')
        plt.ylabel('Flux')
        plt.title('Flux vs Wavelength for Given Spectrum')
        plt.tight_layout()
        plt.show()