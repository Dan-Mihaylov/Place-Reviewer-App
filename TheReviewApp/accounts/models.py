from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='info',
        null=False,
        blank=True
    )

    address_line = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    country = models.CharField(
        max_length=100
        , null=True,
        blank=True
    )

    city = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    photo = models.ImageField(
        upload_to='user_photos/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Info"
