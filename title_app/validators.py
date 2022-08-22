from django.core.exceptions import ValidationError
import re


def validate_russian(text):
    if not bool(re.search('[а-яА-Я]', text)):
        raise ValidationError(
            'Введите русское название/имя',
        )


def validate_english(text):
    if not bool(text.isascii()):
        raise ValidationError(
            'Введите английское название/имя',
        )
