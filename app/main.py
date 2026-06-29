from fastapi import FastAPI

from app.database.database import engine
from app.database.base import Base

from app.routers.auth import router

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hisab Kitaab API",
    description="Expense Tracking Backend API",
    version="1.0.0"
)

@app.get("/")
def home():
    return{"message": "Welcome to Hisab Kitaab API"}

app.include_router(router)