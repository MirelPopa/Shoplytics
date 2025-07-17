from db.main import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class SalesData(Base):
    __tablename__ = "sales_data"

    order_id = Column(String, primary_key=True)
    quantity = Column(Integer, nullable=False)
    timestamp = Column(DateTime)
    price = Column(Float, nullable=False)
    product_id = Column(String, ForeignKey("product.product_id"), nullable=False)

class Product(Base):
    __tablename__ = "product"

    product_id = Column(String, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
