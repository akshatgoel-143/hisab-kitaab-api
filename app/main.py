from fastapi import FastAPI
from app.routers.auth import router

app = FastAPI(
    title="Hisab Kitaab API",
    description="Expense Tracking Backend API",
    version="1.0.0"
)

@app.get("/")
def home():
    return{"message": "Welcome to Hisab Kitaab API"}

app.include_router(router)