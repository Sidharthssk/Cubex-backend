from datetime import datetime, date

import strawberry
from typing import Optional, List
from framework.graphql.types import BaseQuery


@strawberry.type
class ParticipantProfileType:
    id: strawberry.ID
    name: Optional[str] = None
    dob: Optional[date] = None
    phone: Optional[str] = None
    eventID: Optional[strawberry.ID] = None


@strawberry.type
class BasicParticipantType:
    id: strawberry.ID
    name: str
    dob: date
    eventID: strawberry.ID
    age_groupID: strawberry.ID
    contact: str
    email: str


@strawberry.type
class ParticipantQuery(BaseQuery):
    participants: List[BasicParticipantType]


__all__ = ["ParticipantQuery", "BasicParticipantType", "ParticipantProfileType"]
