import gcsfs
import pyarrow

def read_parquet(gs_directory_path, to_pandas=True):
    """
    Reads multiple (partitioned) parquet files from a GS directory
    e.g. 'gs://<bucket>/<directory>' (without ending /)
    """
    gs = gcsfs.GCSFileSystem()
    arrow_df = pyarrow.parquet.ParquetDataset('gs://de-zoomcamp-413815-de-zoomcamp/nyc_yellow_taxi_data', filesystem=gs)
    if to_pandas:
        return arrow_df.read_pandas().to_pandas()
    return arrow_df