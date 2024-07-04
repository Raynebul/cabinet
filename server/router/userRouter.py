from typing import Annotated, Optional

from fastapi import APIRouter, Depends, Body, Request, HTTPException, Response, Cookie
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import sessionmaker, Session
from router.repository import get_db, User, Material, Role
from datetime import datetime, timedelta
from typing import Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session
from router.repository import SessionLocal, get_db
from jose import jwt, JWTError
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext

# from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/user",
    tags=["User"],
)

SECRET_KEY = "aw2324knekajdwjyagjdgj25yawhegnyj2883q2ohoch2c2fer3rda0876fd3368689ere79nbnnnaaaaaaaaaaaaaa"
SECRET_REFRESH_KEY = "aw2324knekajdwjyagjdgj25yarefreshwhegnyj2883q2ohoch2c2fer3rda0876fdrefresh3368689ere79nbnnnaaaaaaaaaaaaaa"
ALGORITHM = ("HS256")
PREFIX = 'Bearer '

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='user/token')


class CreateUserRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


db_dependency = Annotated[Session, Depends(get_db)]


# user_dependency = Annotated[dict, Depends(get_current_user)]

def verify_token(req: Request):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    header = req.headers["Authorization"]
    authorization_access = header
    #authorization_access = req.cookies.get("access_token")  # changed to accept access token from httpOnly Cookie
    print(authorization_access)
    if authorization_access == "" or authorization_access == None:
        return {
            "username": None
        }
    else:
        bearer, _, token = authorization_access.partition(' ')
        # print(token)
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            #raise HTTPException(status_code=403, detail="token has been expired")
            return {
                "username": None
            }
        username: str = payload.get("username")
        user_id: int = payload.get("id")
        email: str = payload.get("email")
        status: str = payload.get("status")
        active: bool = payload.get("active")
        first_name: str = payload.get("first_name")
        last_name: str = payload.get("last_name")
        patronymic: str = payload.get("patronymic")
        telephone: str = payload.get("telephone")
        role: int = payload.get("role")
        user = {}
        user["username"] = username
        user["email"] = email
        user["id"] = user_id
        user["status"] = status
        user["active"] = active
        user["first_name"] = first_name
        user["last_name"] = last_name
        user["patronymic"] = patronymic
        user["telephone"] = telephone
        user["role"] = role
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized"
            )
        return user


@router.get("")
async def get_user(user: str = Depends(verify_token), db: Session = Depends(get_db)):
    print(user)
    new_role = {}
    if(user["username"] != None):
       new_role = db.query(Role).filter(Role.id == user["role"]).first()
    return {"user": user, "role": new_role}
    # query={}


def set_jwt(req: Request):
    header = req.headers["Authorization"]
    bearer, _, token = header.partition(' ')
    # json_compatible_item_data = jsonable_encoder({"jwt": token})
    # response = JSONResponse(content=json_compatible_item_data)
    return token


"""
def delete_jwt(req: Request):
    return {"test": 1}
"""


@router.get("/set_cookies")
async def set_cookies(token: str = Depends(set_jwt)):
    print(token)
    json_compatible_item_data = jsonable_encoder({"jwt": token})
    response = JSONResponse(content=json_compatible_item_data)
    response.set_cookie(key='access_token', value=f"Bearer {token}", httponly=True)
    return response


@router.get("/delete_cookies")
async def delete_cookies(request: Request):
    json_compatible_item_data = {}
    response = JSONResponse(content=json_compatible_item_data)
    expires = datetime.now() + timedelta(seconds=1)
    response.set_cookie(
        key="access_token",
        value="",
        httponly=True,
        expires=expires.strftime("%a, %d %b %Y %H:%M:%S GMT"),
    )
    print(response)
    return response
    # return response
    # print("help me please")
    # response = templates.TemplateResponse("login.html", {"request": request, "title": "Login"})
    # response.delete_cookie("access_token")

    # return {"status": "success"}
    # return {"test": 1}


@router.put("")
async def put_user(data=Body(), db: Session = Depends(get_db)):
    user = data["user"]
    id = user["id"]
    new_user = db.query(User).filter(User.id == id).first()
    new_user.last_name = user["last_name"]
    new_user.first_name = user["first_name"]
    new_user.patronymic = user["patronymic"]
    new_user.email = user["email"]
    new_user.active = user["active"]
    new_user.status = user["status"]
    new_user.telephone = user["telephone"]
    db.commit()  # сохраняем изменения
    db.refresh(new_user)
    print("user", data)
    if not user:
        print(False)
        return {"error": True}
    else:
        access_token = create_access_token(user["username"], user["id"], user["email"], user["active"], user["status"],
                                           user["first_name"], user["last_name"], user["patronymic"], user["telephone"], user["role"],
                                           timedelta(minutes=6*60))
        refresh_token = create_refresh_token(user["username"], user["id"], timedelta(days=20))
    json_compatible_item_data = jsonable_encoder({"user": user, "access_token": access_token,
                                                  "refresh_token": refresh_token})
    now = datetime.now()
    response = JSONResponse(content=json_compatible_item_data)
    print("setting cookies...")
    return {"user": user, "token": access_token}


@router.put("/material")
async def put_material(data=Body(), db: Session = Depends(get_db)):
    metadata = data["metadata"]
    id = data["id"]
    name = data["name"]
    # print(metadata, id, name)
    material = db.query(Material).filter(Material.id == id).first()
    material.name = name
    material.metadata_ = metadata
    db.commit()  # сохраняем изменения
    db.refresh(material)
    return {"metadata": metadata}


@router.get("/material")
async def get_materials(db: Session = Depends(get_db)):
    materials = db.query(Material).all()
    return {"materials": materials}

@router.delete("/material")
async def delete_material(data=Body(), db: Session = Depends(get_db)):
    id = data["id"]
    print(id)
    material = db.query(Material).filter(Material.id == id).first()
    db.delete(material)  # сохраняем изменения
    db.commit()
    #users = db.query(User).all()
    return {"test": True, "material": material}

@router.post("")
async def post_user(data=Body(), db: Session = Depends(get_db)):
    login = data["login"]
    password = data["password"]
    # hashed_password = bcrypt_context.hash(password)
    # print(hashed_password)
    jwt = ""
    token = ""
    expressIn = "120s"
    #print(login, password)
    user = db.query(User).filter((User.password == password and User.username == login) or (
            User.password == password and User.email == login)).first()
    #print('user ', user)
    access_token = ""
    refresh_token = ""
    if not user:
        print(False)
        return {"error": True}
    else:
        access_token = create_access_token(user.username, user.id, user.email, user.active, user.status,
                                           user.first_name, user.last_name, user.patronymic, user.telephone, user.role,
                                           timedelta(minutes=6*60))
        refresh_token = create_refresh_token(user.username, user.id, timedelta(days=20))
        """response.set_cookie(key='access_token', value=f"Bearer {access_token}", httponly=True, secure=True,
                            samesite="none", )"""
        # response.set_cookie(key='test', value=f"test")
    # print(response)
    json_compatible_item_data = jsonable_encoder({"user": user, "access_token": access_token,
                                                  "refresh_token": refresh_token})
    now = datetime.now()
    response = JSONResponse(content=json_compatible_item_data)
    print("setting cookies...")
    return response


def create_access_token(username: str, user_id: int, email: str, active: bool,
                        status: str, first_name: str,
                        last_name: str, patronymic: str, telephone: str, role: int, expires_delta: timedelta):
    payload = {"id": user_id,
               "username": username,
               "email": email,
               "active": active,
               "status": status,
               "first_name": first_name,
               "last_name": last_name,
               "patronymic": patronymic,
               "telephone": telephone,
               "role": role}
    expires = datetime.utcnow() + expires_delta
    payload.update({'exp': expires})
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return access_token


def create_refresh_token(username: str, user_id: int, expires_delta: timedelta):
    payload = {"sub": username, "id": user_id}
    expires = datetime.utcnow() + expires_delta
    payload.update({'exp': expires})
    refresh_token = jwt.encode(payload, SECRET_REFRESH_KEY, algorithm=ALGORITHM)
    return refresh_token


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
