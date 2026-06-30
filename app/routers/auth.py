from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import User
from app.schemas.user import UserRegister, UserLogin
from app.core.security import hash_password, verify_password
from app.core.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/test")
def test():
    return {
        "message": "Auth Router Working"
    }


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.scalar(select(User).where(User.email == user.email))

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "New User Registered Successfully", "user_id": new_user.id}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.scalar(select(User).where(User.email == user.email))

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid Email or Password")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid Email or Password")

    token = create_access_token({"sub": db_user.email})

    return {"access_token": token, "token_type": "bearer"}
