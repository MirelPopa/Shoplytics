with sales as (
    select *
    from {{ source('postgres_data', 'sales_data') }}
)

select
    sum(price) as total_revenue
from sales
