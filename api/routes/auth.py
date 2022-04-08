from datetime import timedelta

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from api.security import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
import core.crud as crud
from sqlalchemy.orm import Session
import core.schemas as schemas

router = APIRouter(
    tags=["Auth"],
    prefix="/api/auth"
)

# linked to oauth2_scheme
@router.post("/login", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(crud.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# @router.post("/register", response_model=Token)
# async def create_user_account(form_data: ):
#     # importance of form data
#     # work on logins first

@router.post("/register", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(crud.get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)