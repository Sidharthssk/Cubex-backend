import strawberry
from typing import Optional


@strawberry.type
class TokenType:
    access: str
    refresh: str

@strawberry.type
class UserProfile:
    id: strawberry.ID
    username: str
    email: str
    role: str
    token: Optional[TokenType] = None


__all__ = [
    'UserProfile', 'TokenType'
]