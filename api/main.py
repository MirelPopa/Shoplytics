from fastapi import FastAPI

fast_api_app = FastAPI()

@fast_api_app.get("/health")
def health_check():
    return {"message": "Health check succeeded"}
