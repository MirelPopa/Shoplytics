with source as (
    select * from {{ source('stg_postgres_data', 'sales_data') }}
),

staged_data as (
    select
        order_id,
        product_id,
        quantity,
        price,
        timestamp
    from source
)

select * from staged_data
