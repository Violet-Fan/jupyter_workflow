import os 
import pandas as pd 
from urllib.request import urlretrieve

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
FILENAME = 'fremont_bicycle.csv'

def get_fremont_bicycle_data(filename = FILENAME , url = URL , force_download = False):
    '''
    download and cache the data
    parameters:
    filename: string, location to save the data 
    url: string, web location of the data 
    force_dwonload: bool, if True, force redownload the data 
    return: 
    data: pandas.DataFrame 
    
    '''
    ##mm force_download=False, os.path.exists
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('fremont_bicycle.csv', index_col='Date', parse_dates=True)
    ## index_col, parse_dates(Timestamp)
    data.columns = ['Total', 'East', 'West']
    ## the columns changed
    return data 
