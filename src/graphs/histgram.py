from nba_api.stats.endpoints import boxscoretraditionalv2

from src.utils import GAME_ID
from fastapi import APIRouter
router = APIRouter()


@router.get("/{game_id}/histgram")
async def histgram(game_id: str = GAME_ID):
    res = boxscoretraditionalv2.BoxScoreTraditionalV2(
        game_id=game_id
    ).get_normalized_dict()
    return res
