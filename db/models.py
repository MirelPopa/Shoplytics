from db.main import Base
from sqlalchemy import Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from datetime import datetime

class SalesData(Base):
    __tablename__ = "sales_data"
    order_id = mapped_column(String, primary_key=True)
    quantity = mapped_column(Integer, nullable=False)
    timestamp = mapped_column(DateTime)
    price = mapped_column(Float, nullable=False)
    product_id = mapped_column(ForeignKey("product.product_id"), nullable=False)

class Product(Base):
    __tablename__ = "product"
    product_id = mapped_column(String, primary_key=True)
    product_name = mapped_column(String, nullable=False)
    price = mapped_column(Float, nullable=False)
