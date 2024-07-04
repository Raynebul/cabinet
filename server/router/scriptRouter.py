from typing import Annotated

from fastapi import APIRouter, Depends, Body
from router.repository import get_db, User, Material, Role
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import insert
import json

router = APIRouter(
    prefix="/script",
    tags=["script"],
)

@router.get("")
def get_script(db: Session = Depends(get_db)):
    users = db.query(User).all()
    length = len(users)
    script_loaded = False
    if length == 0:
        script_loaded = False
    else:
        script_loaded = True
    return {"script_loaded": script_loaded }


@router.post("")
def load_script(data=Body(), db: Session = Depends(get_db)):
    users = []
    roles = []
    materials = []
    with open('data/materials.json', encoding='utf-8') as fh:
        materials = json.load(fh)
    for item in materials:
        new_material = Material(
            IDtext=item["IDtext"], name=item["name"],
            metadata_=json.dumps(item["metadata_"]),

        )
        db.add(new_material)
        db.commit()
        db.refresh(new_material)
    with open('data/users.json', encoding='utf-8') as fh:
        users = json.load(fh)

    for item in users:
        new_user = User(username=item["username"],
                        email=item["email"],
                        password=item["password"],
                        active=item["active"],
                        status=item["status"],
                        first_name=item["first_name"],
                        last_name=item["last_name"],
                        patronymic=item["patronymic"],
                        telephone=item["telephone"],
                        role=item["role"])
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    with open('data/roles.json', encoding='utf-8') as fh:
        roles = json.load(fh)

    for item in roles:
        new_role = Role(name=item["name"],
                            admin=item["admin"],
                            trainer=item["trainer"],
                            course=item["course"],
                            profile=item["profile"]
                            )
        db.add(new_role)
        db.commit()
        db.refresh(new_role)

    return {"users": users, "roles": roles, "materials": materials}
