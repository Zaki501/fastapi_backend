from fastapi import APIRouter, Depends
from core.schemas import User
from api.security import get_current_active_user
import core.schemas as schemas
import core.crud as crud
from sqlalchemy.orm import Session
 
router = APIRouter(
    tags=["User"],
    prefix="/api/user"
)

@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

