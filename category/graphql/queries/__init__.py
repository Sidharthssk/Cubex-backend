from .events import Event
import strawberry

@strawberry.type
class EventQuery(
    Event
):
    pass


__all__ = ["EventQuery", ]
