

  create or replace view `de-zoomcamp-413815`.`dbt_staging`.`my_second_dbt_model`
  OPTIONS()
  as -- Use the `ref` function to select from other models

select *
from `de-zoomcamp-413815`.`dbt_staging`.`my_first_dbt_model`
where id = 1;

