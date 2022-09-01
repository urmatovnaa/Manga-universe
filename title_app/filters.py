from django.forms import CheckboxSelectMultiple
from django_filters import rest_framework as filters

from title_app.models import Tag, Genre, Title, TitleStatus, AdultContent, \
    TranslatorStatus, TitleType, ReleaseFormat


class TitleFilter(filters.FilterSet):
    """ TitleList filters """
    genres = filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all(), widget=CheckboxSelectMultiple(), label="Жанры")
    tags = filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=CheckboxSelectMultiple(), label="Теги")
    min_year = filters.NumberFilter(field_name="year", lookup_expr='gte', label='Год выпуска')
    max_year = filters.NumberFilter(field_name="year", lookup_expr='lte', label='')
    min_chapter = filters.NumberFilter(field_name="chapter", lookup_expr='gte', label='Количество глав')
    max_chapter = filters.NumberFilter(field_name="chapter", lookup_expr='lte', label='')
    adult_content = filters.ModelMultipleChoiceFilter(queryset=AdultContent.objects.all(),
                                                      widget=CheckboxSelectMultiple(), label="Возрастной рейтинг")
    type_title = filters.ModelMultipleChoiceFilter(queryset=TitleType.objects.all(),
                                                   widget=CheckboxSelectMultiple(), label="Тип")
    translator_status = filters.ModelMultipleChoiceFilter(queryset=TranslatorStatus.objects.all(),
                                                   widget=CheckboxSelectMultiple(), label="Статус перевода")
    release_format = filters.ModelMultipleChoiceFilter(queryset=ReleaseFormat.objects.all(),
                                                   widget=CheckboxSelectMultiple(), label="Формат выпуска")
    title_status = filters.ModelMultipleChoiceFilter(queryset=TitleStatus.objects.all(),
                                                   widget=CheckboxSelectMultiple(), label="Статус тайтла")

    class Meta:
        model = Title
        fields = ['genres', 'tags', 'min_year', 'max_year', 'min_chapter', 'max_chapter',
                  'type_title', 'translator_status', 'release_format', 'title_status']


