from typing import Optional, List
import strawberry
from participant.models.participant import Participant


@strawberry.type
class EventType:
    id: strawberry.ID
    name: str
    description: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]

# @strawberry.type
# class EventListType:
#     events: List[Participant.eventList]


__all__ = ["EventType", ]
