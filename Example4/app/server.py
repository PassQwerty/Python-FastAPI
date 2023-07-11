# cd example4/app - перейти в папку
# uvicorn server:app --reload - запустить фаил с перезагрузкой изменений

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index/", response_class=HTMLResponse)
async def read_item(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)