from typing import Optional
import strawberry


@strawberry.type
class AgeGroupType:
    id: strawberry.ID
    name: str
    minAge: int
    maxAge: int


__all__ = ['AgeGroupType']
