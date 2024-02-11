

  create or replace view `de-zoomcamp-413815`.`dbt_abhishek_yadav`.`stg_yellow_trip_data`
  OPTIONS()
  as -- 

select
-- identifiers
to_hex(md5(cast(coalesce(cast(vendorid as string), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(tpep_pickup_datetime as string), '_dbt_utils_surrogate_key_null_') as string))) as tripid,
cast(vendorid as integer) as vendorid,
cast(ratecodeid as integer) as ratecodeid,
cast(pulocationid as integer) as pickup_locationid,
cast(dolocationid as integer) as dropoff_locationid,

-- timestamps
TIMESTAMP_SECONDS(CAST(CAST(tpep_pickup_datetime as INT64)/10000000 AS INT64)) as pickup_datetime,
TIMESTAMP_SECONDS(CAST(CAST(tpep_dropoff_datetime as INT64)/10000000 AS INT64)) as dropoff_datetime,

-- trip info
store_and_fwd_flag,
cast(passenger_count as integer) as passenger_count,
cast(trip_distance as numeric) as trip_distance,
1 as trip_type,

-- payment info
cast(fare_amount as numeric) as fare_amount,
cast(extra as numeric) as extra,
cast(mta_tax as numeric) as mta_tax,
cast(tip_amount as numeric) as tip_amount,
cast(tolls_amount as numeric) as tolls_amount,
cast(0 as numeric) as ehail_fee,
cast(improvement_surcharge as numeric) as improvement_surcharge,
cast(total_amount as numeric) as total_amount,
cast(payment_type as integer) as payment_type,
case cast( payment_type as integer )
        when 1 then 'Credit Card'
        when 2 then 'Cash'
        when 3 then 'No Charge'
        when 4 then 'Dispute'
        when 5 then 'Unknown'
        when 6 then 'Voided Trip'
        else 'Empty'
    end as payment_type_description,
cast(congestion_surcharge as numeric) as congestion_surcharge
from `de-zoomcamp-413815`.`trips_all_data`.`yello_trip_data`
where vendorid is not null
qualify row_number() over(partition by cast(VendorID as string), tpep_pickup_datetime)=1
-- dbt-bq run --select stg_green_tripdata  --var 'is_test_run: false'

limit 100
;

