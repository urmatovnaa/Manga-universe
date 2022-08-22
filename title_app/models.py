from django.db import models
from multiselectfield import MultiSelectField

from title_app.choices import TITLE_STATUS_CHOICES, TRANSLATOR_STATUS_CHOICES, TITLE_TYPE_CHOICES, \
    ADULT_CONTENT_CHOICES, DOWNLOAD_CHAPTER_CHOICES, RELEASE_FORMAT_CHOICES, M
from title_app.validators import validate_russian, validate_english

from admin_panel_app.models import Person, Team

from main.settings import AUTH_USER_MODEL


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             verbose_name='Пользователь',
                             null=True)
    cover = models.ImageField(upload_to='cover/', verbose_name='Обложка',
                              blank=True, null=True)
    background = models.ImageField(upload_to='background/', verbose_name='Фон',
                                   blank=True, null=True)
    origin_name = models.CharField(max_length=100,
                                   verbose_name='Оригинальное название (без иероглифов)',
                                   unique=True)
    russian_name = models.CharField(max_length=100,
                                    verbose_name='Русское название',
                                    validators=[validate_russian],
                                    blank=True, null=True)
    english_name = models.CharField(max_length=100,
                                    verbose_name='Английское название',
                                    validators=[validate_english],
                                    blank=True, null=True)
    alternative_names = models.CharField(max_length=500,
                                         verbose_name='Альтернативные названия (с иероглифами)',
                                         blank=True, null=True)
    title_type = models.CharField(max_length=10,
                                  choices=TITLE_TYPE_CHOICES,
                                  default=M,
                                  verbose_name='Тип',
                                  blank=True, null=True)
    release_year = models.CharField(max_length=4,
                                    verbose_name='Год релиза',
                                    blank=True, null=True)
    title_url = models.SlugField(unique=True, verbose_name='урл манги')
    author = models.ManyToManyField(Person,
                                    verbose_name='Автор',
                                    blank=True,
                                    related_name='author')
    artist = models.ManyToManyField(Person,
                                    verbose_name='Художник',
                                    blank=True,
                                    related_name='artist')
    publisher = models.ManyToManyField(Person,
                                       verbose_name='Издатель',
                                       blank=True,
                                       related_name='publisher')
    genres = models.ManyToManyField(Genre,
                                    verbose_name='Жанр',
                                    blank=True)
    tags = models.ManyToManyField(Tag,
                                  verbose_name='Теги',
                                  blank=True)
    release_format = MultiSelectField(max_length=50,
                                      choices=RELEASE_FORMAT_CHOICES,
                                      max_choices=7,
                                      verbose_name='Формат выпуска',
                                      blank=True, null=True)
    translators = models.ManyToManyField(Team,
                                         verbose_name='Переводчики',
                                         blank=True)
    title_status = models.CharField(max_length=50,
                                    choices=TITLE_STATUS_CHOICES,
                                    verbose_name='Статус тайтла',
                                    blank=True, null=True)
    translator_status = models.CharField(max_length=50,
                                         choices=TRANSLATOR_STATUS_CHOICES,
                                         verbose_name='Статус перевода',
                                         blank=True, null=True)
    adult_content = models.CharField(max_length=50,
                                     choices=ADULT_CONTENT_CHOICES,
                                     verbose_name='Контент для взрослых',
                                     blank=True, null=True)
    download_chapter = models.CharField(max_length=50,
                                        choices=DOWNLOAD_CHAPTER_CHOICES,
                                        verbose_name='Загрузка глав',
                                        blank=True, null=True)
    links_to_original = models.URLField(verbose_name='Ссылки на оригинал или анлейт (помогает модерации)',
                                        blank=True, null=True)
    description = models.CharField(max_length=1000,
                                   verbose_name='Описание',
                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Тайтл'
        verbose_name_plural = 'Тайтлы'

    def __str__(self):
        return self.origin_name
