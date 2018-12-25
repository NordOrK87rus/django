from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):
    avatar = models.ForeignKey(
        'images.Avatar',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        default=0,
        verbose_name='Возраст'
    )

    def __str__(self):
        return self.username
