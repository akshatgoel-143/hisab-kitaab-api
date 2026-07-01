from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.auth import verify_access_token
from app.database.database import get_db
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    email = verify_access_token(token)

    user = db.scalar(
        select(User).where(User.email == email)
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user