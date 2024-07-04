from sqlalchemy import create_engine, text
from typing import AsyncGenerator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from pathlib import Path

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#with engine.connect() as conn:
    #sql = "ALTER TABLE users ADD COLUMN role Integer;"
    #conn.execute(text(sql))

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    active = Column(Boolean, nullable=False)
    status = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    telephone = Column(String)
    role = Column(Integer)


class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    IDtext = Column(String)
    name = Column(String)
    metadata_ = Column(Text)

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    admin = Column(Boolean)
    trainer = Column(Boolean)
    course = Column(Boolean)
    profile = Column(Boolean)



Base.metadata.create_all(bind=engine)



# Material.__table__.drop(engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

