{{ config(
    materialized='view',
    backup=False
) }}


with raw_sales as (
    select *
    from {{ source('postgres_data', 'sales_data') }}
),

sales_by_product as (
    select
        product_id,
        count(*) as total_orders,
        sum(quantity) as total_quantity_sold,
        sum(price) as total_revenue,
        avg(price) as avg_order_value
    from raw_sales
    group by product_id
)

select * from sales_by_product
