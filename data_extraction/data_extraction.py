import pandas as pd
from urllib.parse import quote
import requests
from csv import reader
from io import StringIO

"""Class to facilitate data extraction"""
class DataExtraction:

    """Initializing data to be read in/stored from SDSS Database"""
    def __init__(self, plateid, mjd, fiberid):
        self.data = None
        self.plateid = plateid
        self.mjd = mjd
        self.fiberid = fiberid

    """Function to get spectrum data"""
    def get_spectrum_data(self):
        try:
            response = requests.get(f'https://dr16.sdss.org/optical/spectrum/view/data/format=csv/spec=lite?plateid={self.plateid}&mjd={self.mjd}&fiberid={self.fiberid}')
            if response.status_code == 200:
                data = response.content.decode('utf-8')
                self.data = pd.read_csv(StringIO(data))
                return self.data
            else:
                print("Not able to fetch data. Please check the syntax of your SQL query")
        except requests.RequestException:
                print("There was an error with the request. Please try again.")

    """Function to query the metadata and set the data to a Pandas DataFrame of the output data"""
    def query_metadata(self, query):
        try:
            response = requests.get(f'http://skyserver.sdss.org/dr16/SkyServerWS/SearchTools/SqlSearch?cmd={quote(query)}&format=csv')
            if response.status_code == 200:
                csv_data = response.text
                csv_reader = reader(StringIO(csv_data))

                # Skip first row in output as it is title of table
                next(csv_reader)

                # Get column names
                col_names = next(csv_reader)

                # Aggregate all rows of data from csv output
                rows = []
                for row in csv_reader:
                    rows.append(row)
                
                # Update data
                self.data = pd.DataFrame(rows, columns=col_names)
                return self.data
            else:
                print("Not able to fetch data. Please check the syntax of your SQL query")

        except requests.RequestException:
            print("There was an error with the request. Please try again.")

    """Function to get the metadata for the given spectrum"""
    def get_metadata(self):
        query = f'SELECT * FROM SpecObj WHERE plate={self.plateid} AND mjd={self.mjd} AND fiberid={self.fiberid}'
        self.query_metadata(query)

    """Function to read in a csv file and set the data to a Pandas DataFrame of the file's data"""
    def read_csv_file(self, csv_file_path):
        try:
            self.data = pd.read_csv(csv_file_path, skiprows=1)
            return self.data
        except FileNotFoundError:
            print("File not found, please ensure the file path is correct.")
        except Exception:
            print("Error: Please try again.")