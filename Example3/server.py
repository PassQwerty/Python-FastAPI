# pip install fastapi
# pip install "uvicorn[standard]"
# cd example3 - перейти в папку
# uvicorn server:app --reload - запустить фаил с перезагрузкой изменений

from fastapi import FastAPI
from api.others import other_router
from api.users import user_router
from api.default import default_router

app = FastAPI(
    title="New App with FastAPI",
    description="new application by Vadim Sidorenko",
    version="0.2.0",
)

app.include_router(other_router)
app.include_router(user_router)
app.include_router(default_router)
