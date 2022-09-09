from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from title_app.validators import validate_russian, validate_english
from title_app.choices import DOWNLOAD_CHAPTER_CHOICES

from admin_panel_app.models import Person, Team

from main.settings import AUTH_USER_MODEL


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class TitleType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тип')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class ReleaseFormat(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Формат выпуска')

    class Meta:
        verbose_name = 'Формат выпуска'
        verbose_name_plural = 'Форматы выпуска'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class TitleStatus(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Статус тайтла')

    class Meta:
        verbose_name = 'Статус тайтла'
        verbose_name_plural = 'Статус тайтла'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class TranslatorStatus(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Статус перевода')

    class Meta:
        verbose_name = 'Статус перевода'
        verbose_name_plural = 'Статусы перевода'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class AdultContent(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Возрастной рейтинг')

    class Meta:
        verbose_name = 'Возрастной рейтинг'
        verbose_name_plural = 'Возрастной рейтинг'

    def clean(self):
        self.name = self.name.capitalize()

    def __str__(self):
        return self.name


class Title(models.Model):
    """ Title/Manga model """
    user = models.ManyToManyField(AUTH_USER_MODEL,
                                  verbose_name='Пользователь')
    cover = models.ImageField(upload_to='cover/',
                              verbose_name='Обложка',
                              blank=True, null=True)
    background = models.ImageField(upload_to='background/',
                                   verbose_name='Фон',
                                   blank=True, null=True)
    russian_name = models.CharField(max_length=100,
                                    verbose_name='Русское название',
                                    validators=[validate_russian],
                                    blank=True, null=True)
    english_name = models.CharField(max_length=100,
                                    verbose_name='Английское название',
                                    validators=[validate_english],
                                    unique=True)
    alternative_names = models.CharField(max_length=500,
                                         verbose_name='Альтернативные названия (с иероглифами)',
                                         blank=True, null=True)
    title_type = models.ForeignKey(TitleType,
                                   models.SET_NULL,
                                   verbose_name='Тип',
                                   default='манга',
                                   blank=True, null=True)
    release_year = models.CharField(max_length=4,
                                    verbose_name='Год релиза',
                                    blank=True, null=True)
    title_url = models.SlugField(unique=True,
                                 verbose_name='урл манги',
                                 blank=True, null=True)
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
                                    related_name='genres',
                                    blank=True)
    tags = models.ManyToManyField(Tag,
                                  verbose_name='Теги',
                                  related_name='tags',
                                  blank=True)
    release_format = models.ManyToManyField(ReleaseFormat,
                                            verbose_name='Формат выпуска',
                                            related_name='release_format',
                                            blank=True)
    translators = models.ManyToManyField(Team,
                                         verbose_name='Переводчики',
                                         related_name='translators',
                                         blank=True)
    title_status = models.ForeignKey(TitleStatus,
                                     models.SET_NULL,
                                     verbose_name='Статус тайтла',
                                     blank=True, null=True)
    translator_status = models.ForeignKey(TranslatorStatus,
                                          models.SET_NULL,
                                          verbose_name='Статус перевода',
                                          blank=True, null=True)
    adult_content = models.ForeignKey(AdultContent,
                                      models.SET_NULL,
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
    date_created = models.DateTimeField(verbose_name='Дата создания',
                                        default=timezone.now)

    class Meta:
        verbose_name = 'Тайтл'
        verbose_name_plural = 'Тайтлы'

    def __str__(self):
        return self.english_name

    def save(self, *args, **kwargs):
        self.title_url = slugify(self.english_name)
        super(Title, self).save(*args, **kwargs)


class Rating(models.Model):
    """ Title Rating """
    RATE_CHOICES = (
        (1, '1'), (2, '2'),
        (3, '3'), (4, '4'),
        (5, '5'),
    )
    title = models.ForeignKey(Title,
                              on_delete=models.CASCADE,
                              verbose_name='Тайтл',
                              related_name='rate')
    user = models.ForeignKey(AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    star = models.IntegerField(verbose_name='Рейтинг', choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.star} - {self.title.english_name} by {self.user.username}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = (("title", "user"),)
