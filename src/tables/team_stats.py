from nba_api.stats.endpoints import boxscoretraditionalv2
from fastapi import Request
from src.tables import templates
from src.utils import GAME_ID, make_response
from dataclasses import dataclass
from fastapi import APIRouter
router = APIRouter()


@dataclass
class TeamStats:
    GAME_ID: str
    TEAM_ID: int
    TEAM_NAME: str
    TEAM_ABBREVIATION: str
    TEAM_CITY: str
    MIN: float
    FGM: int
    FGA: int
    FG_PCT: float
    FG3M: int
    FG3A: int
    FG3_PCT: float
    FTM: int
    FTA: int
    FT_PCT: float
    OREB: int
    DREB: int
    REB: int
    AST: int
    STL: int
    BLK: int
    TO: int
    PF: int
    PTS: int
    PLUS_MINUS: float


@dataclass
class View:
    AWAY: TeamStats
    HOME: TeamStats

    @classmethod
    def from_boxscoretraditionalv2_teamstats(cls, l):
        AWAY: TeamStats = TeamStats(**l[0])
        HOME: TeamStats = TeamStats(**l[1])
        return cls(AWAY, HOME)


@router.get("/{game_id}/team_stats")
async def team_stats(request: Request, game_id: str = GAME_ID):
    res = boxscoretraditionalv2.BoxScoreTraditionalV2(
        game_id=game_id
    ).get_normalized_dict()

    view: View = View.from_boxscoretraditionalv2_teamstats(res['TeamStats'])
    view_dict = make_response(request, view)

    view_dict['debug'] = view

    return templates.TemplateResponse(
        'team_stats.html',
        view_dict,
    )
