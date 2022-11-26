from typing import List

from framework.graphql.types import BaseOffsetQuery
from participant.graphql.types import BasicParticipantType
from category.graphql.types import EventType
import strawberry


@strawberry.type
class ScoreboardType:
    id: strawberry.ID
    duration: str
    participant: BasicParticipantType
    event: EventType


@strawberry.type
class ScoreType:
    participant: BasicParticipantType
    duration: str
    rank: int


@strawberry.type
class ScoreboardQuery(BaseOffsetQuery):
    scores: List[ScoreType]


__all__ =["ScoreboardType", "ScoreType", "ScoreboardQuery", ]
