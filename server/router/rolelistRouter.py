from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import sessionmaker, Session
from router.repository import get_db, User, Role
from sqlalchemy import Column, Integer, String, Boolean, Text

router = APIRouter(
    prefix="/rolelist",
    tags=["Rolelist"],
)

"""
def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN IF NOT EXISTS %s %s' % (table_name, column_name, column_type))
"""
#column = Column('role', Integer)
#add_column(engine, 'users', column)

@router.get("")
def get_rolelist(db: Session = Depends(get_db)):
    """"""
    #with db.engine.begin() as conn:
        #column = Column('role', Integer)
        #add_column(conn, 'users', column)
        #conn.commit()
    roles = db.query(Role).all()
    return {"roles": roles}

@router.post("")
def post_role(data=Body(), db: Session = Depends(get_db)):
    role = data["role"]
    print(role)
    new_role = Role(name=role["name"],
                    admin=role["admin"],
                    trainer=role["trainer"],
                    course=role["course"],
                    profile=role["profile"]
                    )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return {"test": True, "role": new_role}

@router.put("")
def put_rolelist(data=Body(), db: Session = Depends(get_db)):
    role = data["role"]
    id = role["id"]
    new_role = db.query(Role).filter(Role.id == id).first()
    new_role.name = role["name"]
    new_role.admin = role["admin"]
    new_role.trainer = role["trainer"]
    new_role.course = role["course"]
    new_role.profile = role["profile"]
    db.commit()  # сохраняем изменения
    db.refresh(new_role)
    return {"test": True}


@router.delete("")
def delete_rolelist(data=Body(), db: Session = Depends(get_db)):
    id = data["id"]
    role = db.query(Role).filter(Role.id == id).first()
    db.delete(role)  # сохраняем изменения
    db.commit()
    roles = db.query(Role).all()
    return {"roles": roles}
