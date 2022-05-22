from dataclasses import dataclass, asdict
from fastapi import Request

# MIL@BOS GAME5
GAME_ID = "0042100217"


def make_response(req: Request, dc: dataclass) -> dict:
    d: dict = asdict(dc)
    d['request'] = req
    return d
