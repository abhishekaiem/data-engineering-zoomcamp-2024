import gcsfs
import pyarrow
import pyarrow.parquet as pq
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def read_parquet():
    """
    Reads multiple (partitioned) parquet files from a GS directory
    e.g. 'gs://<bucket>/<directory>' (without ending /)
    """
    gs = gcsfs.GCSFileSystem()
    arrow_df = pq.ParquetDataset('gs://de-zoomcamp-413815-de-zoomcamp/nyc_yellow_taxi_data', filesystem=gs)
    if to_pandas:
        return arrow_df.read_pandas().to_pandas()
    return arrow_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
