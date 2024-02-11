docker run --rm \
    -p 5050:5050 \
    -v ~/.google/credentials/google_credentials_2024.json:/.google/credentials/google_credentials_2024.json \
    -v ~/.dbt/profiles.yml:/root/.dbt/profiles.yml \
    $(docker build -q . -t dbt-service)