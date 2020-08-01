from jupyter.data import get_fremont_bicycle_data
import pandas as pd 
##mm error 
## data = get_fremont_bicycle_data()
def test_fremont_data():
    URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
    FILENAME = 'fremont_bicycle.csv'
    data = get_fremont_bicycle_data(FILENAME, URL)
    assert all(data.columns == ['Total', 'East', 'West'])
    assert isinstance(data.index, pd.DatetimeIndex)