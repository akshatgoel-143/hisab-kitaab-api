from fastapi import APIRouter, Depends

from app.core.response import success_response
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    return success_response(
        message="User fetched successfully",
        data={
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email
        }
    )