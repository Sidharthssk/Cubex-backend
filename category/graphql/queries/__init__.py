from .events import Event
from .ageGroup import AgeGroup
import strawberry

@strawberry.type
class EventQuery(
    Event,
    AgeGroup
):
    pass


__all__ = ["EventQuery", ]
