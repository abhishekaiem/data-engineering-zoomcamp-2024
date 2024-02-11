select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select tripid
from `de-zoomcamp-413815`.`dbt_abhishek_yadav`.`stg_yellow_trip_data`
where tripid is null



      
    ) dbt_internal_test