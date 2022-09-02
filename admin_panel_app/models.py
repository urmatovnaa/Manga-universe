from django.db import models

from main.settings import AUTH_USER_MODEL


class Contacts(models.Model):
    """ Model for connection with admins """
    text = models.CharField(max_length=500, verbose_name='Текст')
    url = models.URLField(verbose_name='Свяжитесь с нами', blank=True, null=True)
    url2 = models.URLField(verbose_name='Свяжитесь с нами', blank=True, null=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.text


class News(models.Model):
    """ Model for site-news """
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
                             verbose_name='Пользователь',
                             null=True)
    date = models.DateField(auto_now=True,
                            verbose_name='Дата')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=250,
                            verbose_name='Название темы',
                            unique=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class FAQ(models.Model):
    """ Model for Frequently Asked Question(s) """
    user = models.ForeignKey(AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             verbose_name='Пользователь',
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

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'

    def __str__(self):
        return f'{self.question}-{self.answer}'


class Person(models.Model):
    """ Model for author, artist, publisher """
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

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персоны'

    def __str__(self):
        return self.english_name


class Team(models.Model):
    """ Model for teams/translators """
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
                                     blank=True)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name

