import pytest
from unittest.mock import patch, Mock
import numpy as np
import pandas as pd
from .data_preprocessing import PreProcessing

@pytest.fixture
def mock_data_extraction():
    patch_path = 'data_preprocessing.data_preprocessing.DataExtraction'
    with patch(patch_path) as mock:  
        curr_instance = mock.return_value
        data = {
            'Wavelength': np.linspace(100, 200, 100),
            'Flux': np.random.rand(100)
        }
        curr_instance.get_spectrum_data.return_value = pd.DataFrame(data)
        new_data = {'z': [0.05]}
        curr_instance.get_metadata.return_value = pd.DataFrame(new_data)
        yield curr_instance

def test_redshift(mock_data_extraction):
    plateid = 234
    mjd = 664
    fiberid = 153
    preprocess = PreProcessing(plateid=plateid, mjd=mjd, fiberid=fiberid)
    preprocess.redshift_correction()
    assert 'Emit Wavelength' in preprocess.data.columns

def test_norm(mock_data_extraction):
    plateid = 234
    mjd = 664
    fiberid = 153
    preprocess = PreProcessing(plateid=plateid, mjd=mjd, fiberid=fiberid)
    preprocess.normalization()
    assert preprocess.data.shape[1] == 2 


def test_inter(mock_data_extraction):
    plateid = 234
    mjd = 664
    fiberid = 153
    preprocess = PreProcessing(plateid=plateid, mjd=mjd, fiberid=fiberid)
    preprocess.outlier_removal()
    wavelengths = np.linspace(200, 400, 25) 
    result = preprocess.interpolation(wavelengths)
    assert isinstance(result, pd.DataFrame)
    assert len(result) == len(wavelengths)


def test_inter_waveemtpy(mock_data_extraction):
    plateid = 234
    mjd = 664
    fiberid = 153
    preprocess = PreProcessing(plateid=plateid, mjd=mjd, fiberid=fiberid)
    result = preprocess.interpolation([])
    assert result is None or result.empty