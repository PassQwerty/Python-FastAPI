# pip install fastapi
# pip install "uvicorn[standard]"
# cd example1 - перейти в папку
# uvicorn server:app --reload - запустить фаил с перезагрузкой изменений

from typing import Union
from fastapi import FastAPI

app = FastAPI(
    title="New App with FastAPI",
    description="new application by Vadim Sidorenko",
    version="0.2.0",
)

dataBaseUsers = [
    {"id": 1, "role": "admin", "name": "Vasya"},
    {"id": 2, "role": "user", "name": "Ivan"},
    {"id": 3, "role": "user", "name": "Arkadiy"}
]


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in dataBaseUsers:
        if user.get("id") == user_id:
            return user


@app.get("/usersall")
async def get_user_all():
    return dataBaseUsers


@app.post("/useradd/{user_name}")
async def post_user1(user_name: str):
    countDataBaseUsers = len(dataBaseUsers)
    countDataBaseUsers += 1
    new_user = {"id": countDataBaseUsers, "role": "user", "name": user_name}
    dataBaseUsers.append(new_user)
    return {"status": 200, "data": new_user}


@app.post("/user/changename")
async def post_change_name(user_name: str, new_name: str):
    user = [user for user in dataBaseUsers if user.get("name") == user_name][0]
    user["name"] = new_name
    return {"status": 200, "data": user}
