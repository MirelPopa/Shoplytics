with raw_sales as (
    select *
    from {{ source('postgres_data', 'sales_data') }}
),

sales_by_day as (
    select
        date_trunc('day', timestamp) as sales_day,
        count(*) as total_orders,
        sum(quantity) as total_quantity,
        sum(price) as total_revenue,
        avg(price) as avg_order_value
    from raw_sales
    group by 1
)

select * from sales_by_day
