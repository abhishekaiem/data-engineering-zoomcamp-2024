if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(f"Data before preprocessing is {data.shape}")
    print(f"data with zero passenger: {data['passenger_count'].isin([0]).sum()}")
    print(f"data with no distance: {data['trip_distance'].isin([0]).sum()}")
    print(data[(data['trip_distance']>0)&(data['passenger_count']>0)].shape)
    
    print(f"missing data :{data[~((data['trip_distance'].isin([0]))&(data['passenger_count'].isin([0])))].shape}")
    print(data.columns.str.contains('ID').sum())
    data = data[(data['trip_distance']>0)&(data['passenger_count']>0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.columns = data.columns.str.replace('ID', '_id').str.lower()
    print(data.passenger_count.isin([0]).sum())
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert output.columns.isin(['vendor_id']).any() and output.passenger_count.isin([0]).sum()==0 and output.trip_distance.isin([0]).sum()==0
    # assert output.passenger_count.isin([0]).sum()==0
    # assert output.trip_distance.isin([0]).sum()==0
