
  
    

    create or replace table `de-zoomcamp-413815`.`production`.`dim_zones`
      
    
    

    OPTIONS()
    as (
      select 
locationid,
borough,
zone,
replace(service_zone, 'Boro', 'Green') as service_zone
from `de-zoomcamp-413815`.`dbt_staging`.`taxi_zone_lookup`
    );
  