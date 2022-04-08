# interact with the database

from sqlalchemy.orm import Session

import core.models as models
import core.schemas as schemas
from api.security import hash_password


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_all_users():
    pass


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)

    db_user = models.User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        disabled=False,
        hashed_password=hashed_password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
