import strawberry
from typing import Optional

@strawberry.type
class UserProfile:
    id: strawberry.ID
    username: str
    email: str
    role: str

__all__ = [
    'UserProfile',
]