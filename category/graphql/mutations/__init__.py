from .events import EventMutation
import strawberry

@strawberry.type
class EventMutations(
    EventMutation
):
    pass


__all__ = [
    'EventMutations'
]