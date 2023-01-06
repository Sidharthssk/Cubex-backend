from datetime import datetime, date

import strawberry
from typing import Optional, List
from framework.graphql.types import BaseQuery
from category.graphql.types import EventType, AgeGroupType


@strawberry.type
class ParticipantProfileType:
    id: strawberry.ID
    name: Optional[str] = None
    dob: Optional[date] = None
    contact: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    ageGroup: Optional[AgeGroupType] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    ageGroup: Optional[AgeGroupType] = None
    events: List[EventType]


@strawberry.type
class BasicParticipantType:
    id: strawberry.ID
    name: str
    dob: date
    contact: str
    email: str


@strawberry.type
class ParticipantQuery(BaseQuery):
    participants: List[BasicParticipantType]


__all__ = ["ParticipantQuery", "BasicParticipantType", "ParticipantProfileType"]
