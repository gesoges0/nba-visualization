from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from graphs import histgram

app = FastAPI()
app.include_router(histgram.router)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def live(request: Request):
    """この日の試合を表敬式で表示する"""
    hoge = "fuga"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "hoge": hoge,
        },
    )
