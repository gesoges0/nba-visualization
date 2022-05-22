from fastapi import APIRouter
from nba_api.stats.endpoints import boxscoretraditionalv2

from src.utils import GAME_ID

router = APIRouter()


@router.get("/{game_id}/boxscoretraditionalv2")
async def log_boxscoretraditionalv2(game_id: str = GAME_ID):
    res = boxscoretraditionalv2.BoxScoreTraditionalV2(
        game_id=game_id
    ).get_normalized_dict()
    return res
