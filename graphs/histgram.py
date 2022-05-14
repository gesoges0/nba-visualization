from fastapi import APIRouter
from nba_api.stats.endpoints import boxscoretraditionalv2

from graphs.utils import GAME_ID

router = APIRouter()


@router.get("/histgram")
async def histgram():
    res = boxscoretraditionalv2.BoxScoreTraditionalV2(
        game_id=GAME_ID
    ).get_normalized_dict()
    # PlayerStats, TeamStats, TeamStarterBenchStats
    return res["PlayerStats"]
