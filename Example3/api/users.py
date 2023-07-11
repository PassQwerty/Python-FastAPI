from fastapi import APIRouter
from models import User

user_router = APIRouter(prefix='/users', tags=['User'])


@user_router.get("/")
async def get_users():
    return {"status": 200, "message": f"view all users"}


@user_router.get("/{user_id}")
async def get_user(user_name: str):
    return {"status": 200, "message": f"Hello {user_name}"}


@user_router.post("/{user_name}")
async def create_user(user: User):
    return {"status": 200, "message": f"Create user:{user.name}"}


@user_router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"status": 200, "message": f"Delete user id:{user_id}"}


@user_router.put("/{user_id}")
async def update_user(user_id: int):
    return {"status": 200, "message": f"Update user id:{user_id}"}
