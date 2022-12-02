from typing import Optional
import strawberry


@strawberry.type
class EventType:
    id: strawberry.ID
    name: str
    description: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]


__all__ = ["EventType", ]
