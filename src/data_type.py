# from dataclasses import dataclass
# from typing import Optional
#
#
# @dataclass
# class TraditionalTeamStats:
#     FGM: int
#     FGA: int
#     FG_PCT: float
#     FG3M: int
#     FG3A: int
#     FG3_PCT: float
#     FTM: int
#     FTA: int
#     FT_PCT: float
#     OREB: int
#     DREB: int
#     REB: int
#     AST: int
#     STL: int
#     BLK: int
#     TO: int
#     PF: int
#     PTS: int
#     PLUS_MINUS: float
#
#
# @dataclass
# class Team:
#     TEAM_ID: int
#     TEAM_NAME: str
#     TEAM_ABBREVIATION: str
#     TEAM_CITY: str
#
#
# @dataclass
# class MetaTraditionalTeamStats:
#     GAME_ID: str
#     AWAY_TEAM: Team
#     HOME_TEAM: Team
#     AWAY_TEAM_STATS: TraditionalTeamStats
#     HOME_TEAM_STATS: TraditionalTeamStats
#
#     @classmethod
#     def from_dict(cls, l: list[dict]):
#         away_team_stats = l[0]
#         home_team_stats = l[1]
#         return cls(
#             GAME_ID=away_team_stats['GAME_ID'],
#             AWAY_TEAM=Team(),
#             HOME_TEAM=Team(),
#             AWAY_TEAM_STATS=away_team_stats[]
#         )
#
#
#
# # @dataclass
# # class TraditionalStats:
# #     GAME_ID: str
# #     TEAM_ID: int
# #     TEAM_ABBREVIATION: str
# #     TEAM_CITY: str
# #     PLAYER_ID: int
# #     PLAYER_NAME: str
# #     NICKNAME: str
# #     START_POSITION: str
# #     COMMENT: str
# #     MIN: Optional[str]
# #     FGM: Optional[int]
# #     FGA: Optional[int]
# #     FG_PCT: Optional[float]
# #     FG3M: Optional[int]
# #     FG3A: Optional[int]
# #     FG3_PCT: Optional[float]
# #     FTM: Optional[int]
# #     FTA: Optional[int]
# #     FT_PCT: Optional[float]
# #     OREB: Optional[int]
# #     DREB: Optional[int]
# #     REB: Optional[int]
# #     AST: Optional[int]
# #     STL: Optional[int]
# #     BLK: Optional[int]
# #     TO: Optional[int]
# #     PF: Optional[int]
# #     PTS: Optional[int]
# #     PLUS_MINUS: Optional[float]
# #
# #     @classmethod
# #     def from_dict(cls, d: dict):
# #         return cls(**d)
# #
# #     def get_stats_only(self) -> dict:
# #         pass