from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.graphs import histgram
from src.logs import log_boxscoretraditionalv2
from src.tables import team_stats
from src.utils import GAME_ID

app = FastAPI()
app.include_router(histgram.router)
app.include_router(log_boxscoretraditionalv2.router)
app.include_router(team_stats.router)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/{game_id}", response_class=HTMLResponse)
async def index(request: Request, game_id: str = GAME_ID):
    """この日の試合を表敬式で表示する"""

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "game_id": game_id,
        },
    )
