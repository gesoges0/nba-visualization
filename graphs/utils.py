from dataclasses import dataclass
from typing import Optional

# MIL@BOS GAME5
GAME_ID = "0042100215"


class TraditionalStats:
    GAME_ID: str
    TEAM_ID: int
    TEAM_ABBREVIATION: str
    TEAM_CITY: str
    PLAYER_ID: int
    PLAYER_NAME: str
    NICKNAME: str
    START_POSITION: str
    COMMENT: str
    MIN: Optional[str]
    FGM: Optional[int]
    FGA: Optional[int]
    FG_PCT: Optional[float]
    FG3M: Optional[int]
    FG3A: Optional[int]
    FG3_PCT: Optional[float]
    FTM: Optional[int]
    FTA: Optional[int]
    FT_PCT: Optional[float]
    OREB: Optional[int]
    DREB: Optional[int]
    REB: Optional[int]
    AST: Optional[int]
    STL: Optional[int]
    BLK: Optional[int]
    TO: Optional[int]
    PF: Optional[int]
    PTS: Optional[int]
    PLUS_MINUS: Optional[float]
