import pytest
from unittest.mock import patch, Mock
from .machine_learning import MachineLearning
import pandas as pd
import numpy as np

@pytest.fixture
def mock_data_extraction():
    with patch('data_extraction.data_extraction.DataExtraction') as mock:
        instance = mock.return_value
        data = {'Wavelength': np.arange(100, 124), 'Flux': np.random.rand(24)}
        final_data = pd.DataFrame(data)
        instance.get_spectrum_data.return_value = final_data
        instance.query_metadata.return_value = None
        new_data = pd.DataFrame({'class': ['GALAXY', 'STAR', 'QSO']})
        instance.data = new_data
        yield instance

def test_generate(mock_data_extraction):
    ml = MachineLearning()
    ml.generate_ml_data()
    ml_len = len(ml.data)
    assert ml.data is not None
    assert 'Class' in ml.data.columns
    
def test_split():
    ml = MachineLearning()
    test_data = {'Wavelength': np.arange(100, 124), 'Flux': np.random.rand(24), 'Class': ['GALAXY', 'STAR', 'QSO'] * 8}
    ml.data = pd.DataFrame(test_data)
    ml.train_test_split()
    X_test_val = ml.X_test
    y_test_val  = ml.y_test
    assert X_test_val is not None
    assert y_test_val is not None




def test_pred(mock_data_extraction):
    ml = MachineLearning()
    ml.generate_ml_data()
    ml.train_test_split()
    ml.fit()

    arr = np.array(['GALAXY', 'STAR'])

    with patch.object(ml.model, 'predict', return_value=arr):
        pred = ml.X_test
        total_predictions = ml.predict(pred)
        assert total_predictions is not None

def test_pred_prob(mock_data_extraction):
    ml = MachineLearning()
    ml.generate_ml_data()
    ml.train_test_split()
    ml.fit()

    arr = np.array([[0.8, 0.2], [0.1, 0.9]])

    with patch.object(ml.model, 'predict_proba', return_value=arr):
        pred = ml.X_test
        total_pred = ml.predict_proba(pred)
        assert total_pred is not None

def test_confusion_mat(mock_data_extraction):
    ml = MachineLearning()
    ml.generate_ml_data()
    ml.train_test_split()
    ml.fit()

    y_actual, y_predictions = ['GALAXY', 'STAR'], ['STAR', 'GALAXY']
    matrix = ml.generate_confusion_matrix(y_actual, y_predictions)
    assert matrix is not None
    shape = matrix.shape
    assert shape == (2, 2)


def test_null_train_test():
    ml = MachineLearning()
    ml.train_test_split()
    x_train = ml.X_train
    assert x_train is None  

def test_fit_no_train_test_split():
    ml = MachineLearning()
    ml.fit()
    assert ml.model is None  

def test_pred_no_model():
    ml = MachineLearning()
    data = {'Wavelength': [100], 'Flux': [10]}
    final_data = pd.DataFrame(data)
    pred = ml.predict(final_data)
    assert pred is None  

def test_prob_pred_no_model():
    ml = MachineLearning()
    data = {'Wavelength': [100], 'Flux': [10]}
    final_data = pd.DataFrame(data)
    prob_pred = ml.predict_proba(final_data)
    assert prob_pred is None  


def test_gen_confusion_matrix_null():
    ml = MachineLearning()
    matrix = ml.generate_confusion_matrix(None, None)
    assert matrix is None  