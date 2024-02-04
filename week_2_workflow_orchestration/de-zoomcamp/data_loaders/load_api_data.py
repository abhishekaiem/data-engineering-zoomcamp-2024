import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz'

    # parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
    # return pd.read_csv(url, sep=',', compression='gzip', parse_dates=parse_dates)
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_'

    year = 2020
    start = 10
    end = 12
    data = pd.DataFrame()
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    for month in range(start, end+1):
        url = f'{base_url}{year}-{month:02d}.csv.gz'
        print(month)
        df = pd.read_csv(url, sep=',', compression='gzip', parse_dates=parse_dates)
        print(df.shape)
        data = pd.concat([df, data])
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
