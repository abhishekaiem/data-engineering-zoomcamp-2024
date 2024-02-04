## Build docker image

docker build -t test:pandas .

## Run a docker image

docker run -it test:pandas

docker run -it \
  -e POSTGRES_USER=root \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_DB=ny_taxi \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5434:5434 \
  postgres:13

URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

python upload_data.py \
  --user=root \
  --password=root \
  --host=host.docker.internal \
  --port=5432 \
  --db_name=ny_taxi \
  --table_name=yellow_taxi_data \
  --url=${URL}

8986775b85152730abd647d32bb3bee73612f032f6af15b82d6224cb2f14e71e

docker run -it \
  --network=2_docker_sql_default \
  test:pandas \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db_name=ny_taxi \
    --table_name=yellow_taxi_data  \
    --url=${URL}