import numpy as np
import pandas as pd
from fracdiff.sklearn import Fracdiff
from data_extraction.data_extraction import DataExtraction


class DataAugmentation:
    """
    A class to perform data augmentation by computing derivatives using fractional differentiation.

    Attributes:
    - data: DataFrame to hold the spectrum data.
    
    Methods:
    - get_spectrum_data: Fetches spectrum data using plate ID, MJD, and fiber ID.
    - get_from_csv: Loads spectrum data from a CSV file.
    - data_augmentation: Computes derivatives of spectrum data using fractional differentiation.
    """
    def __init__(self):
        """
        Initializes a DataAugmentation object instance.
        """
        self.data = None
    
    def get_spectrum_data(self, plateid, mjd, fiberid):
        """
        Fetches spectrum data using plate ID, MJD, and fiber ID.

        Args:
        - plateid (int): Plate ID of the spectrum data.
        - mjd (int): MJD (Modified Julian Date) of the spectrum data.
        - fiberid (int): Fiber ID of the spectrum data.

        Fetches spectrum data using DataExtraction class and assigns it to self.data.
        """
        self.data = DataExtraction(plateid, mjd, fiberid).get_spectrum_data()

    def get_from_csv(self, path):
        """
        Loads spectrum data from a CSV file.

        Args:
        - path: Path to the CSV file containing spectrum data.

        Loads spectrum data from a CSV file.
        """
        self.data = pd.read_csv(path)

    def data_augmentation(self, alpha=0.5):
        """
        Computes derivatives of spectrum data using fractional differentiation.
        Args:
        - alpha: Fractional order for differentiation.
        Computes derivatives of spectrum data using the fracdiff library.
        """
        x = np.array(self.data['Wavelength'])
        y = np.array(self.data['Flux'])
        x = x.reshape(-1, 1)
        model = Fracdiff(d=alpha)
        model.fit(x, y)
        dy_dx = model.transform(x)
        new_col_name = f'Derivative: {alpha}'
        self.data[new_col_name] = dy_dx
        return self.data