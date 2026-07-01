from fastapi import FastAPI
from app.database.database import engine
from app.database.base import Base
from app.routers.auth import router
from app.routers.user import router as user_router
from app.core.exception_handler import register_exception_handlers

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hisab Kitaab API",
    description="Expense Tracking Backend API",
    version="1.0.0"
)

register_exception_handlers(app)

@app.get("/")
def home():
    return{"message": "Welcome to Hisab Kitaab API"}

app.include_router(router)

app.include_router(user_router)