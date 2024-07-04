from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import sessionmaker, Session
from router.repository import get_db, User

router = APIRouter(
    prefix="/userlist",
    tags=["Userlist"],
)


@router.get("")
def get_userlist(db: Session = Depends(get_db)):
    """"""
    users = db.query(User).all()
    print(users)
    return {"users": users}

@router.put("/user_settings")
def put_new_usersettings(data=Body(), db: Session = Depends(get_db)):
    user = data["user"]
    print(user["active"])
    id = user["id"]
    new_user = db.query(User).filter(User.id == id).first()
    print(new_user.role)
    new_user.active = user["active"]
    new_user.last_name = user["last_name"]
    new_user.first_name = user["first_name"]
    new_user.patronymic = user["patronymic"]
    new_user.email = user["email"]
    new_user.status = user["status"]
    new_user.telephone = user["telephone"]
    new_user.role = user["role"]
    db.commit()  # сохраняем изменения
    db.refresh(new_user)
    print(user)
    return {"test": True}

@router.put("")
def put_userlist(data=Body(), db: Session = Depends(get_db)):
    user = data["user"]
    id = user["id"]
    new_user = db.query(User).filter(User.id == id).first()
    if new_user.active == False:
        new_user.active = True
    else:
        new_user.active = False
    db.commit()  # сохраняем изменения
    db.refresh(new_user)
    return {"user": new_user}


@router.delete("")
def delete_userlist(data=Body(), db: Session = Depends(get_db)):
    id = data["id"]
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)  # сохраняем изменения
    db.commit()
    users = db.query(User).all()
    return {"users": users}
