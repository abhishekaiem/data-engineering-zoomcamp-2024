import io
import pandas as pd
import datetime
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
    base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_'
    # https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet
    print(pd.__version__)
    year = 2022
    start = 1
    end = 12
    data = pd.DataFrame()
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    for month in range(start, end+1):
        url = f'{base_url}{year}-{month:02d}.parquet'
        # print(url)
        df = pd.read_parquet(url, engine='pyarrow')
        # print(df.shape)
        df['lpep_pickup_datetime'] = df['lpep_pickup_datetime'].astype('str')
        # df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
        df['lpep_dropoff_datetime'] = df['lpep_dropoff_datetime'].astype('str')
        # df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'], unit='ms')
        # df.lpep_dropoff_datetime = df.lpep_dropoff_datetime.apply(lambda d: datetime.datetime.fromtimestamp(int(str(d))).strftime('%Y-%m-%d'))
        data = pd.concat([df, data])
    # print(data.dtypes)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
