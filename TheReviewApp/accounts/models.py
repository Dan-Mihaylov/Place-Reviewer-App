from django.db import models

from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Group, Permission


class PlaceUser(auth_models.AbstractBaseUser):

    username = models.CharField(
        max_length=50,
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
    )

    last_name = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        unique=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    can_add_places = models.BooleanField(
        default=True,
        editable=False,
    )

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.first_name
