
    
    

with child as (
    select pickup_locationid as from_field
    from `de-zoomcamp-413815`.`dbt_abhishek_yadav`.`stg_yellow_trip_data`
    where pickup_locationid is not null
),

parent as (
    select locationid as to_field
    from `de-zoomcamp-413815`.`dbt_staging`.`taxi_zone_lookup`
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


