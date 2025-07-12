from fastapi import FastAPI
from db.utils import generate_fake_sales

fast_api_app = FastAPI()

@fast_api_app.get("/health")
def health_check():
    return {"message": "Health check succeeded"}

@fast_api_app.get("/sales")
def get_sales():
    generated_records_list = generate_fake_sales(5)
    return generated_records_list

