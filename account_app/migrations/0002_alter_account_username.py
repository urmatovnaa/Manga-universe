# Generated by Django 4.1 on 2022-09-23 11:28

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким username уже существует.'}, max_length=60, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Никнейм'),
        ),
    ]
