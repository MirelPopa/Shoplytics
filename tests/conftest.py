import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.main import Base
from db.models import Product, SalesData
import os

# Use env var or fallback to localhost
db_url = os.getenv("DATABASE_URL", "postgresql://admin_user:admin_pass@localhost:5432/datastitcher")
engine = create_engine(db_url)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def test_db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def clean_test_data(test_db_session):
    # Clean relevant tables before each test
    test_db_session.query(SalesData).delete()
    test_db_session.query(Product).delete()
    test_db_session.commit()
    yield
    # Optional: cleanup again after test
    test_db_session.query(SalesData).delete()
    test_db_session.query(Product).delete()
    test_db_session.commit()
