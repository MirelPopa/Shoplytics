from db.utils import generate_fake_sales
from db.models import SalesData, Product

def test_generate_fake_sales_creates_valid_data(test_db_session, clean_test_data):
    generate_fake_sales(n=5)

    sales = test_db_session.query(SalesData).all()
    assert len(sales) == 5
    assert all(s.product_id for s in sales)
    assert all(s.price > 0 for s in sales)

def test_sales_data_foreign_key_consistency(test_db_session, clean_test_data):
    # test if the product ids from the sales_data table are indeed present in the product table
    generate_fake_sales(n=10)

    product_ids = {p.product_id for p in test_db_session.query(Product).all()}
    for sale in test_db_session.query(SalesData).all():
        assert sale.product_id in product_ids
