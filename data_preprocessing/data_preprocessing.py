from scipy.interpolate import interp1d
from sklearn.preprocessing import StandardScaler
from data_extraction.data_extraction import DataExtraction
import pandas as pd

"""Class for pre-processing spectral data"""
class PreProcessing:

    """Initializing spectral data and metadata"""
    def __init__(self, plateid, mjd, fiberid):
        self.data_extraction = DataExtraction(plateid, mjd, fiberid)
        self.data = self.data_extraction.get_spectrum_data()
        self.metadata = self.data_extraction.get_metadata()

    """Function to perform redshift correction and compute Emit Wavelength"""
    def redshift_correction(self):
        # Redshift Correction based on formula
        if self.data is not None:
            self.data['Emit Wavelength'] = self.data['Wavelength'] / (1 + float(self.metadata['z'][0]))
        else:
            print("Error: Please ensure you have inputted a valid spectrum.")

    """Function to perform data normalization"""
    def normalization(self):
        scaler = StandardScaler()
        cols = ['Wavelength', 'Flux']
        if self.data is not None:
            self.data[cols] = scaler.fit_transform(self.data[cols])
            self.data = self.data[cols]
        else:
            print("Error: Please ensure you have inputted a valid spectrum.")

    """Function to perform outlier removal"""
    def outlier_removal(self):
        if self.data is not None:
            # Wavelength outlier removal
            lower_bound = self.data['Wavelength'].quantile(0.25)
            upper_bound = self.data['Wavelength'].quantile(0.75)
            self.data = self.data[(self.data['Wavelength'] >= lower_bound) & (self.data['Wavelength'] <= upper_bound)].reset_index(drop=True)

            # Flux outlier removal
            lower_bound = self.data['Flux'].quantile(0.25)
            upper_bound = self.data['Flux'].quantile(0.75)
            self.data = self.data[(self.data['Flux'] >= lower_bound) & (self.data['Flux'] <= upper_bound)].reset_index(drop=True)
        else:
            print("Error: Please ensure you have inputted a valid spectrum.")

    """Function to perform interpolation"""
    def interpolation(self, wavelengths):
        if (self.data is not None) and (len(wavelengths) > 0):
            func = interp1d(self.data['Wavelength'], self.data['Flux'], kind='linear', fill_value="extrapolate")
            flux = func(wavelengths)
            return pd.DataFrame({'Wavelength': wavelengths, 'Flux': flux})
        else:
            print("Error: Please ensure you have inputted a valid spectrum and valid wavelengths to the function.")