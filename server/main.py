from typing import Optional, Annotated

from fastapi import FastAPI, Depends, Body, status, Response, Request, Cookie
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from fastapi_users import fastapi_users, FastAPIUsers

"""

from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, Session
from router.repository import SessionLocal, Base, User, Material
"""

from router.repository import SessionLocal, Base, User, Material

import router.userRouter as user_router
import router.userlistRouter as userlist_router
import router.reset_passwordRouter as reset_password_router
import router.registerRouter as register_router
import router.loginRouter as login_router
import router.metadataRouter as metadata_router
import router.rolelistRouter as rolelist_router
import router.scriptRouter as script_router

import json

# создание движка

app = FastAPI()

# origins = ["*"]
origins = ["http://localhost:5000", "http://localhost:8000", "http://localhost:5173", "http://localhost:4173",
           "http://localhost:4000", "http://clio.ws"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)
app.include_router(userlist_router.router)
app.include_router(reset_password_router.router)
app.include_router(register_router.router)
app.include_router(login_router.router)
app.include_router(metadata_router.router)
app.include_router(rolelist_router.router)
app.include_router(script_router.router)

@app.get("/")
def root(last_visit: str | None = Cookie(default=None)):
    if last_visit == None:
        return {"message": "Это ваш первый визит на сайт"}
    else:
        return {"message": f"Ваш последний визит: {last_visit}"}


"""def root():
    now = datetime.now()    # получаем текущую дату и время
    response = JSONResponse(content={"message": "куки установлены"})
    response.set_cookie(key="last_visit", value=now, path="/user")
    return response"""


@app.post("/")
def root_post(response: Response):
    now = datetime.now()  # получаем текущую дату и время
    print(now)
    #response = JSONResponse(content=jsonable_encoder({"message": "куки установлены"}))
    response.set_cookie(key="last_visit", value=f"{now}", httponly=True)
    return {"message": "куки установлены"}
