import strawberry
from typing import Optional


@strawberry.input
class ScoreboardInput:
    duration: str
    eventID: strawberry.ID
    participantID: strawberry.ID


__all__ = ["ScoreboardInput", ]
