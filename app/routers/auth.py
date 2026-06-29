from fastapi import APIRouter
from app.schemas.user import UserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/test")
def test():
    return {"message": "Auth Router Working"}

@router.post("/register")
def register(user: UserRegister):
    return user   