select 
locationid,
borough,
zone,
replace(service_zone, 'Boro', 'Green') as service_zone
from `de-zoomcamp-413815`.`dbt_staging`.`taxi_zone_lookup`