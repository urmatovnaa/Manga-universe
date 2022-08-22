from django.db import models

from main.settings import AUTH_USER_MODEL


class Contacts(models.Model):
    text = models.CharField(max_length=500, verbose_name='Текст')
    url = models.URLField(verbose_name='Свяжитесь с нами', blank=True, null=True)
    url2 = models.URLField(verbose_name='Свяжитесь с нами', blank=True, null=True)


class News(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name='Заголовок')
    text = models.CharField(max_length=2000,
                            verbose_name='Текст',
                            blank=True, null=True)
    file = models.FileField(upload_to='news',
                            verbose_name='Файл или изображение',
                            blank=True, null=True)
    user = models.ForeignKey(AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True)
    date = models.DateField(auto_now=True,
                            verbose_name='Дата')


class Topic(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name='Название темы',
                            unique=True)


class FAQ(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True)
    topic = models.ForeignKey(Topic,
                              on_delete=models.CASCADE,
                              verbose_name='Тема')
    question = models.CharField(max_length=100,
                                verbose_name='Вопрос')
    answer = models.CharField(max_length=2000,
                              verbose_name='Ответ',
                              blank=True, null=True)
    photo = models.FileField(upload_to='FAQ photos',
                             verbose_name='Файл или изображение',
                             blank=True, null=True)


class Person(models.Model):
    english_name = models.CharField(max_length=60,
                                    verbose_name='Имя на английском (без иероглифов)',
                                    unique=True)
    russian_name = models.CharField(max_length=60,
                                    verbose_name='Имя на русском',
                                    blank=True, null=True)
    alternative_names = models.CharField(max_length=255,
                                         verbose_name='Известен так же под именем',
                                         blank=True, null=True)
    description = models.CharField(max_length=500,
                                   verbose_name='Описание',
                                   blank=True, null=True)
    photo = models.ImageField(upload_to='person',
                              verbose_name='Файл или изображение',
                              blank=True, null=True)


class Team(models.Model):
    cover = models.ImageField(upload_to='cover/', verbose_name='Обложка',
                              blank=True, null=True)
    name = models.CharField(max_length=100,
                            verbose_name='Название',
                            unique=True)
    team_url = models.SlugField(unique=True, verbose_name='урл команды')
    site = models.URLField(verbose_name='Сайт',
                           blank=True, null=True)
    vk = models.URLField(verbose_name='Группа VK',
                         blank=True, null=True)
    description = models.CharField(max_length=500,
                                   verbose_name='Описание',
                                   blank=True, null=True)
    discord = models.URLField(verbose_name='Discord сервер',
                              blank=True, null=True)
    members = models.ManyToManyField(AUTH_USER_MODEL, verbose_name='УЧАСТНИКИ',
                                     blank=True, null=True)

