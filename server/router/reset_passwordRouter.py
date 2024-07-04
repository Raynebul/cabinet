from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import sessionmaker, Session
from router.repository import get_db, User

router = APIRouter(
    prefix="/reset_password",
    tags=["Reset_password"],
)


@router.put("")
def put_password(data=Body(), db: Session = Depends(get_db)):
    user = data["user"]
    print(user)
    id_ = user["id"]
    new_user = db.query(User).filter(User.id == id_).first()
    password = data["newPassword"]
    new_user.password = password
    db.commit()  # сохраняем изменения
    db.refresh(new_user)
    print("user", data)
    return {"user": user}
