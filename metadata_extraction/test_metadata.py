# import necessary librarires
import pytest
from unittest.mock import patch, MagicMock
from metadata import MetadataExtraction
import pandas as pd
from pandas.testing import assert_frame_equal
import requests

def test_initialize():
    assert MetadataExtraction(4055, 55359, 596).data is None

def test_nonexistent_cols():
    extract_data = MetadataExtraction(4055, 55359, 596)
    extract_data.data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})

    with pytest.raises(Exception):
        extract_data.get_cols(['col1', 'nonexistent_col'])

def test_identifiers():
    extract_data = MetadataExtraction(4055, 55359, 596)
    extract_data.data = pd.DataFrame({"specObjID": [123, 456], "col2": [3, 4]})

    res = extract_data.get_identifiers()
    df = pd.DataFrame({"specObjID": [123, 456]})
    
    assert_frame_equal(res, df)

def test_coords():
    extract_data = MetadataExtraction(4055, 55359, 596)
    extract_data.data = pd.DataFrame({"ra": [1.0, 2.0], "dec": [3.0, 4.0]})

    res = extract_data.get_coordinates()
    df = pd.DataFrame({"ra": [1.0, 2.0], "dec": [3.0, 4.0]})
    assert_frame_equal(res, df)

def test_redshift():
    extract_data = MetadataExtraction(4055, 55359, 596)
    extract_data.data = pd.DataFrame({"z": [1.0, 2.0], "zErr": [3.0, 4.0]})

    res = extract_data.get_redshift()
    df = pd.DataFrame({"z": [1.0, 2.0], "zErr": [3.0, 4.0]})
    assert_frame_equal(res, df)
    
def test_class():
    extract_data = MetadataExtraction(4055, 55359, 596)
    extract_data.data = pd.DataFrame({"class": [1.0, 2.0], "zErr": [3.0, 4.0]})

    res = extract_data.get_class()
    df = pd.DataFrame({"class": [1.0, 2.0]})
    assert_frame_equal(res, df)
    