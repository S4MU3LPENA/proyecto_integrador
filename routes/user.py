from fastapi import APIRouter, status
from config.db import conn
from models.user import users
from models.products import products
from schemas.user import User, UserCount
from typing import List
from cryptography.fernet import Fernet


user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)
URL = '/users'

@user.get(
    URL,
    tags=["users"],
    response_model=List[User],
    description="Get a list of all users",
)
async def get_users():
   return conn.execute(users.select()).fetchall()

@user.get(
    URL + "/{id}",
    tags=["users"],
    description="Get a single user by Id",
)
def get_user(id: str):
    user = conn.execute(users.select().where(users.c.id == id)).first()
    
    if user is None:
        return { "estatus": status.HTTP_404_NOT_FOUND, "mesage": "El usuario no fue encontrado"}
    
    return user


@user.post(URL, tags=["users"], response_model=User, description="Create a new user")
def create_user(user: User):
    new_user = {"name": user.name, "username": user.username}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.put(
    URL + "/{id}", tags=["users"], response_model=User, description="Update a User by Id"
)
def update_user(user: User, id: int):
    conn.execute(
        users.update()
        .values(name=user.name, username=user.username, password=user.password)
        .where(users.c.id == id)
    )
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.delete(URL + "/{id}", tags=["users"], status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()
