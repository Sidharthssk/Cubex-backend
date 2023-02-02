from typing import Optional
import strawberry


@strawberry.type
class AgeGroupType:
    id: strawberry.ID
    name: str
    minAge: Optional[int] = None
    maxAge: Optional[int] = None


__all__ = ['AgeGroupType']
