from chowkidar.models import AbstractRefreshToken
from django.db import models


class RefreshToken(AbstractRefreshToken, models.Model):
    pass


__all__ = [
    'RefreshToken'
]