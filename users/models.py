from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ Пользователь. """

    name = models.CharField(unique=True, max_length=200, verbose_name='имя')
    email = models.EmailField(unique=True, verbose_name='email')
    phone_num = models.CharField(max_length=15, blank=True, null=True, verbose_name='номер')
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name='аватар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='добавлен')

    telega_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='телеграм ID')

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['name']
