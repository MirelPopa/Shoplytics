import csv
import argparse
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import text
from faker import Faker
from random import uniform, choice, randint
from db.main import generate_tables, get_db_context
from db.models import SalesData, Product
from pathlib import Path


fake = Faker()

def generate_fake_sales(n=1000):
    with get_db_context() as db:
        insert_products_in_db()
        products_list = get_existing_product_list()
        records_list = []
        for _ in range(n):
            current_product: Product = choice(products_list)
            order_id = fake.unique.uuid4()
            quantity = randint(1, 10)
            price = current_product.price * quantity
            timestamp = fake.date_time_between(start_date="-1y", end_date="now")
            product_id = current_product.product_id
            record = SalesData(
                order_id=order_id,
                quantity=quantity,
                price=price,
                product_id=product_id,
                timestamp=timestamp
            )

            db.add(record)
            records_list.append(record)
        db.commit()

        row_count = db.execute(text("SELECT COUNT(*) FROM sales_data")).scalar()
        print(f"Row count after insert: {row_count}")

        print(f"Successfully inserted {n} records into sales_data.")

def generate_fake_products(n=10):
    PRODUCT_NAMES = [
        "Wireless Mouse", "Bluetooth Speaker", "LED Monitor",
        "USB-C Hub", "Gaming Chair", "Smart Thermostat",
        "Noise Cancelling Headphones", "Portable SSD", "Fitness Tracker"
    ]
    with get_db_context() as db:
        for _ in range(n):
            product_id = fake.unique.uuid4()
            product_name = choice(PRODUCT_NAMES)
            price = round(uniform(10.0, 5000.0), 2)

            product = Product(
                product_id=product_id,
                product_name = product_name,
                price=price
            )
            db.add(product)

        db.commit()
        print(f"Successfully inserted {n} records into product.")

def insert_products_in_db():
    script_dir = Path(__file__).resolve().parent.parent
    csv_path = script_dir / "seeds" / "products.csv"
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        complete_data_dict = csv.DictReader(csvfile)
        with get_db_context() as db:
            complete_data_dict = list(complete_data_dict)
            statement = insert(Product).values(complete_data_dict).on_conflict_do_nothing(index_elements=["product_id"])
            db.execute(statement)
            db.commit()

def get_existing_product_list():
    with get_db_context() as db:
        product_list = db.query(Product).all()
        if not product_list:
            generate_fake_products()
            product_list = db.query(Product).all()
        return product_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--products", type=int, help="Number of products to generate")
    parser.add_argument("--orders", type=int, help="Number of orders to generate")
    parser.add_argument("--insert_products_from_csv", type=bool, help="Insert the products listed in the csv file from the seeds folder")
    args = parser.parse_args()

    generate_tables()

    if args.products:
        generate_fake_products(args.products)
    if args.orders:
        generate_fake_sales(args.orders)
    if args.insert_products_from_csv:
        insert_products_in_db()
