from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import sessionmaker, Session
from router.repository import get_db, User

router = APIRouter(
    prefix="/register",
    tags=["Register"],
)

@router.post("")
def post_user(data=Body(), db: Session = Depends(get_db)):
    user = data["user"]
    new_user = User(username=user["username"],
                    email=user["email"],
                    password=user["password"],
                    active=user["active"],
                    status=user["status"],
                    first_name=user["first_name"],
                    last_name=user["last_name"],
                    patronymic=user["patronymic"],
                    telephone=user["telephone"],
                    role=user["role"]
                    )
    print(user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"test": True, "user": new_user}
