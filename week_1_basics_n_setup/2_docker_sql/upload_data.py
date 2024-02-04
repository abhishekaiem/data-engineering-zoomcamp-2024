import pandas as pd
import os
import argparse
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db_name = params.db_name
    table_name = params.table_name
    url = params.url
    file_name = "output.parquet"

    os.system(f"wget {url} -O {file_name}")
    df = pd.read_parquet(file_name, engine="pyarrow")
    print(df.head())
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")
    engine.connect()
    print("connection is established")
    df.to_sql(table_name, con=engine, if_exists="replace")
    print("Data loaded successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest parquet data to PG")
    # user
    # password
    # host
    # port
    # database Name
    # table Name
    # URL of the parquet  https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet
    parser.add_argument("--user", help="User name of the database")
    parser.add_argument("--password", help="Password of the database")
    parser.add_argument("--host", help="Host name of the database")
    parser.add_argument("--port", help="Port of the database")
    parser.add_argument("--db_name", help="DB name")
    parser.add_argument("--table_name", help="Table Name of the database")
    parser.add_argument("--url", help="url of the file")

    args = parser.parse_args()
    main(args)
