from typing import Optional
import strawberry


@strawberry.type
class EventType:
    id: strawberry.ID
    name: str


__all__ = ["EventType", ]
