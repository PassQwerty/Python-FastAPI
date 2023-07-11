from fastapi import APIRouter

default_router = APIRouter(tags=['Default'])


@default_router.get("/")
async def read_root():
    return {"status": "server started..."}
