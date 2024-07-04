from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import sessionmaker, Session
from router.repository import get_db, User

router = APIRouter(
    prefix="/login",
    tags=["Login"],
)


@router.post("")
def post_user(data=Body(), db: Session = Depends(get_db)):
    login = data["login"]
    password = data["password"]
    user = db.query(User).filter((User.password == password and User.username == login) or (
            User.password == password and User.email == login)).first()
    print(user)
    return {"user": user}
