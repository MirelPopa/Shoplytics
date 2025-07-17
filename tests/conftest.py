import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.main import Base
from sqlalchemy import text
import os

db_url = os.getenv("DATABASE_URL", "postgresql://admin_user:admin_pass@localhost:5432/datastitcher")
engine = create_engine(db_url)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield

@pytest.fixture()
def test_db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def clean_test_data(test_db_session):
    test_db_session.execute(text("TRUNCATE TABLE sales_data RESTART IDENTITY CASCADE;"))
    test_db_session.commit()
    yield
    test_db_session.execute(text("TRUNCATE TABLE sales_data RESTART IDENTITY CASCADE;"))
    test_db_session.commit()
