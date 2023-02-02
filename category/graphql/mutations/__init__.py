from .events import EventMutation
from .ageGroup import AgeGroupMutation
import strawberry


@strawberry.type
class EventMutations(
    EventMutation, AgeGroupMutation
):
    pass


__all__ = [
    'EventMutations'
]