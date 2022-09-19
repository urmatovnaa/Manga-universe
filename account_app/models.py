from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone

from account_app.managers import MyAccountManager, get_default_profile_image


class Account(AbstractUser):
    """ My user model """
    GENDER_CHOICES = [
        ('Noname', 'Не указан'),
        ('M', 'Мужской'),
        ('F', 'Женский')
    ]

    username_validator = UnicodeUsernameValidator()
    first_name = None
    last_name = None

    username = models.CharField(max_length=60,
                                unique=True,
                                validators=[username_validator],
                                error_messages={
                                    "unique": "Пользователь с таким username уже существует."},
                                verbose_name='Никнейм')
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='avatar',
                                      null=True, blank=True,
                                      default=get_default_profile_image,
                                      verbose_name='Аватар')
    background = models.ImageField(upload_to='background',
                                   verbose_name='Фон профиля',
                                   null=True, blank=True)
    info = models.CharField(max_length=255,
                            verbose_name='О себе',
                            blank=True, null=True)
    gender = models.CharField(max_length=20,
                              choices=GENDER_CHOICES,
                              verbose_name='Пол',
                              blank=True, null=True)
    date_joined = models.DateField(verbose_name='Дата регистрации',
                                   default=timezone.now)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'
