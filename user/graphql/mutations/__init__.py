from .mutations import UserMutations as userMutations
import strawberry

@strawberry.type
class UserMutations(
    userMutations
):
    pass


__all__ = [
    'UserMutations'
]
