from typing import Optional, List
import strawberry


@strawberry.input
class ParticipantFilterInput:
    eventID: Optional[strawberry.ID] = None
    categoryID: Optional[strawberry.ID] = None
    age_group: Optional[strawberry.ID] = None
    isOnline: Optional[bool] = None


__all__ = ["ParticipantFilterInput"]


