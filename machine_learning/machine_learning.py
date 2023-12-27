from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
from data_extraction.data_extraction import DataExtraction
from metadata_extraction.metadata import MetadataExtraction

"""Class for Logistic Regression Machine Learning Model"""
class MachineLearning:

    """Initializing data for use in machine learning model and model itself"""
    def __init__(self):
        self.data = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.model = None

    """Function to generate data for machine learning model"""
    def generate_ml_data(self):
        data_extractor = DataExtraction(4055, 55359, 596)
        df = data_extractor.get_spectrum_data()
        wavelength = df['Wavelength'][:24]
        flux = df['Flux'][:24]
        
        classes = []
        for i in range(596, 620):
            data_extractor.query_metadata(f'SELECT * FROM SpecObj WHERE plate=4055 AND mjd=55359 AND fiberID={i}')
            classes.append(data_extractor.data['class'][0])

        self.data = pd.DataFrame({"Wavelength": wavelength, "Flux": flux, "Class": classes})

    """Function to perform train-test split for model"""
    def train_test_split(self):
        if self.data is not None:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data[["Wavelength", "Flux"]], self.data["Class"], test_size=0.33, random_state=42)
        else:
            print("Error: Please generate data before proceeding.")

    """Function to fit model on train data"""
    def fit(self):
        if (self.X_train is not None) and (self.y_train is not None):
            self.model = LogisticRegression(random_state=42).fit(self.X_train, self.y_train)
        else:
            print("Error: Please ensure you have generated the data and performed a train-test split.")

    """Function to generate model predictions given input"""
    def predict(self, X):
        if self.model is None or X is None:
            print("Error: Model not trained or invalid input data.")
            return None
        return self.model.predict(X)

    def predict_proba(self, X):
        if self.model is None or X is None:
            print("Error: Model not trained or invalid input data.")
            return None
        return self.model.predict_proba(X)

    """Function to generate confusion matrix"""
    def generate_confusion_matrix(self, y, y_pred):
        if (y is not None) and (y_pred is not None):
            return confusion_matrix(y, y_pred)
        else:
            print("Error: Please input valid arguments for generating a confusion matrix.")