from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from app.database.database import get_db
from app.models.user import User
from app.schemas.user import UserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.get("/test")
def test():
    return {"message": "Auth Router Working"}

@router.post("/register")
def register(user: UserRegister, db: session = Depends(get_db)):
    new_user = User(
        name = user.name,
        email = user.email,
        password = user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return{
        "message":"New User Registered Successfully",
        "user_id": new_user.id
    }   