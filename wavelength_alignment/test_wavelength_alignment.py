import pytest
from unittest.mock import patch, Mock
import pandas as pd
from .wavelength_alignment import WavelengthAlign
from io import StringIO

@pytest.fixture
def test_data():
    return "Wavelength,Flux\n200,20\n400,40\n600,60"


def test_spectrum_data(test_data):
    # get sample data
    plate_id = 4512
    mjd = 78345
    fiber_id = 900
    patch_ref = 'data_extraction.data_extraction.requests.get'

    with patch(patch_ref) as mock_get:
        # mock the resposne
        mock_response = Mock()
        mock_response.status_code, mock_response.content.decode.return_value = 200, test_data
        mock_get.return_value = mock_response

        wa = WavelengthAlign()
        wa.get_spectrum_data(plate_id, mjd, fiber_id)

        # convert for comparison
        test_data_IO = StringIO(test_data)
        assert wa.data.equals(pd.read_csv(test_data_IO))


def test_align(test_data):
    min_wavelength, max_wavelength = 800, 1000
    expected_aligned_wavelengths = [800, 900, 1000]

    wa = WavelengthAlign()

    wa.data = pd.read_csv(StringIO(test_data))
    aligned_data = wa.align_data(min_wavelength, max_wavelength)

    assert all(aligned_data['Aligned_Wavelength'] == expected_aligned_wavelengths)


def test_empty_align():
    wa = WavelengthAlign()
    assert wa.align_data(400, 500) is None 