import strawberry
from typing import Optional

from framework.graphql.exceptions import APIError
from chowkidar.wrappers import issue_tokens_on_login, revoke_tokens_on_logout
from user.graphql.types import UserProfile

@strawberry.type
class UserMutations:
    @strawberry.field
    def create_score_enterer(self, username: str, email: str, password: str) -> UserProfile:
        from user.models import User
        if User.objects.filter(role=2).count() > 6:
            raise APIError(code='MAX_SCORE_ENTERER_REACHED', message='Maximum score enterers reached')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return UserProfile(
            id=user.id,
            username=user.username,
            email=user.email,
            role=user.role
        )

    @strawberry.field
    def create_admin(self, username: str, email: str, password: str) -> UserProfile:
        from user.models import User
        if User.objects.filter(role=1).count() > 2:
            raise APIError(code='TOO_MANY_ADMINS', message='Too many admins')
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        return UserProfile(
            id=user.id,
            username=user.username,
            email=user.email,
            role=user.role
        )

    @strawberry.mutation
    @issue_tokens_on_login
    def login(self, info, email: str, password: str) -> UserProfile:
        from django.contrib.auth import authenticate
        user = authenticate(email=email, password=password)
        if user is None:
            info.context.LOGIN_USER = None
            raise APIError(code='INVALID_CREDENTIALS', message='Invalid credentials')

        info.context.LOGIN_USER = user
        return UserProfile(
            id=user.id,
            username=user.username,
            email=user.email,
            role=user.role
        )

    @strawberry.field
    @revoke_tokens_on_logout
    def logout(self, info) -> bool:
        info.context.LOGOUT_USER = True
        return True


__all__ = [
    'UserMutations'
]