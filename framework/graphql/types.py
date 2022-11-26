import json
import strawberry
from typing import Any, Optional, NewType, List


@strawberry.type
class BaseOffsetQuery:
    totalCount: Optional[int]
    hasNext: bool


@strawberry.type
class BaseQuery(BaseOffsetQuery):
    lastCursor: Optional[str]


__all__ = [
    'BaseQuery',
    'BaseOffsetQuery'
]

