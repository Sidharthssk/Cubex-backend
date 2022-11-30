from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from user.managers import CustomUserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    ADMIN = 1
    SCORE_ENTERER = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (SCORE_ENTERER, 'Score Enterer'),
    )

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=SCORE_ENTERER)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


__all__ = ['User']
