import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager


DB_HOST = os.getenv("DB_HOST", "postgres")
DB_URL = os.getenv("DATABASE_URL", f"postgresql://admin_user:admin_pass@{DB_HOST}:5432/datastitcher")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def _get_session_local():
    db = SessionLocal()
    return db

def get_db():
    db = _get_session_local()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_db_context():
    db = _get_session_local()
    try:
        yield db
    finally:
        db.close()

def generate_tables():
    Base.metadata.create_all(bind=engine)
