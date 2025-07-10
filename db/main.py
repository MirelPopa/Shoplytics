import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DB_HOST = os.getenv("DB_HOST", "postgres")
DB_URL = os.getenv("DATABASE_URL", f"postgresql://admin_user:admin_pass@{DB_HOST}:5432/datastitcher")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
