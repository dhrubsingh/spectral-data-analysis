import pytest
from .visualization import VisualizeSpectra
import pandas as pd
from unittest.mock import patch, Mock  # Import Mock here

path_to_data_extraction = 'visualization.visualization.DataExtraction' 

@pytest.fixture
def test_data():
    dict_ret = {'Wavelength': [1, 2, 3], 'Flux': [10, 20, 30]}
    return pd.DataFrame(dict_ret)

# get the plot properties in reverse order from it showing
@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.tight_layout')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.grid')
@patch('matplotlib.pyplot.plot')
def test_visualize(plot, grid, xlabel, ylabel, title, tight_layout, show, test_data):
    visualize = VisualizeSpectra()
    visualize.data = test_data
    visualize.visualize()

    # test each field of the plot
    plot.assert_called_once_with(test_data['Wavelength'], test_data['Flux'])
    grid.assert_called_once_with(True)
    xlabel.assert_called_once_with('Wavelength')
    ylabel.assert_called_once_with('Flux')
    title.assert_called_once_with('Flux vs Wavelength for Given Spectrum')
    tight_layout.assert_called_once()
    show.assert_called_once()

def test_csv_data_retreive(test_data, tmpdir):
    csv = tmpdir.join("test.csv")
    test_data.to_csv(csv, index=False)
    viz = VisualizeSpectra()
    viz.get_data_from_csv(csv)

    assert viz.data.equals(test_data)


def test_get_spectrum_data(test_data):
    # put sample data
    plate_data_id = 1234
    data_mjd = 56789
    fiber_test_id = 100

    # get the patch call
    patch_call = patch(path_to_data_extraction)

    with patch_call as extract:
        curr_extract = Mock()
        curr_extract.get_spectrum_data.return_value, extract.return_value = test_data, curr_extract

        visualize = VisualizeSpectra()
        visualize.get_spectrum_data(plate_data_id, data_mjd, fiber_test_id)

        curr_extract.get_spectrum_data.assert_called_once_with()
        assert visualize.data.equals(test_data)

