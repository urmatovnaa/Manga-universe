from django.db import models
from django.db.models import Count

from multiselectfield import MultiSelectField

from main.settings import AUTH_USER_MODEL
from title_app.models import Title


CRITERION_CHOICES = (
        ('same genres', 'По жанрам'),
        ('same panache', 'По рисовке'),
        ('same plot', 'По сюжету'))


class SimilarTitle(models.Model):
    main_title = models.ForeignKey(Title, on_delete=models.CASCADE,
                                   verbose_name='Главный тайтл ', related_name='similar_titles')
    title = models.ForeignKey(Title, on_delete=models.SET_NULL,
                              verbose_name='Похожий тайтл', related_name='sim_title', null=True)
    criterion = MultiSelectField(max_length=25,
                                 choices=CRITERION_CHOICES,
                                 max_choices=2,
                                 verbose_name='Выбрать критерий схожести (макс. 2)')

    class Meta:
        verbose_name = 'Похожее'
        verbose_name_plural = 'Похожее'
        unique_together = (("main_title", "title"),)

    def __str__(self):
        return f'{self.title} - {self.main_title} - {self.criterion}'


class SimilarLike(models.Model):
    similar = models.ForeignKey(SimilarTitle, models.CASCADE, related_name='likes')
    user = models.ForeignKey(AUTH_USER_MODEL, models.SET_NULL, null=True)


class SimilarDislike(models.Model):
    similar = models.ForeignKey(SimilarTitle, models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(AUTH_USER_MODEL, models.SET_NULL, null=True)


# class RelatedTitle(models.Model):
    # CRITERION_CHOICES = (
    #     ('same genres', 'По жанрам'),
    #     ('same panache', 'По рисовке'),
    #     ('same plot', 'По сюжету'))
    # main_title = models.ForeignKey(Title, on_delete=models.CASCADE,
    #                                verbose_name='Главный тайтл ', related_name='similar_titles')
    # title = models.ForeignKey(Title, on_delete=models.SET_NULL,
    #                           verbose_name='Похожий тайтл', related_name='sim_title', null=True)
    # criterion = MultiSelectField(max_length=25,
    #                              choices=CRITERION_CHOICES,
    #                              max_choices=2,
    #                              verbose_name='Выбрать критерий схожести (макс. 2)')

    # class Meta:
    #     verbose_name = 'Похожее'
    #     verbose_name_plural = 'Похожее'
    #     unique_together = (("main_title", "title"),)
    #
    # def __str__(self):
    #     return f'{self.title} - {self.main_title} - {self.criterion}'





# class related:
# 	title(с которым связан)
# 	title(тот самый связанный)
# 	related_type(choices)
# class  statistics:
# 	folder
# 	count
# 	persent
# class rating:
# 	star
# 	count
# 	persent
