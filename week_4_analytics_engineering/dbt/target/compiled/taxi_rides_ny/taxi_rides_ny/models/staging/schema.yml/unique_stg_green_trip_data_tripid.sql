
    
    

with dbt_test__target as (

  select tripid as unique_field
  from `de-zoomcamp-413815`.`dbt_staging`.`stg_green_trip_data`
  where tripid is not null

)

select
    unique_field,
    count(*) as n_records

from dbt_test__target
group by unique_field
having count(*) > 1

