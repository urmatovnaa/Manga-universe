from rest_framework import serializers

from title_app.models import Title, Rating, Genre, Tag, ReleaseFormat

from admin_panel_app.models import Person, Team
from info_section_app.serializers import SimilarSerializer, RelatedSerializer


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class TranslatorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ['name']


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['english_name']


class ReleaseFormatSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReleaseFormat
        fields = '__all__'


class TitleRatingSerializer(serializers.ModelSerializer):
    """ Serializer for create/update Title Rating """

    class Meta:
        model = Rating
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'title': {'read_only': True}
        }

    def create(self, validated_data):
        rate, _ = Rating.objects.update_or_create(
            user=validated_data.get('user', None),
            title_id=validated_data.get('title', None),
            defaults={'star': validated_data.get("star")}
        )
        return rate


class TitleDetailSerializer(serializers.ModelSerializer):
    """ Serializer for unchangeable TitleDetail """
    rate = TitleRatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=4, decimal_places=2)
    title_status_name = serializers.CharField(read_only=True)
    translator_status_name = serializers.CharField(read_only=True)
    adult_content_name = serializers.CharField(read_only=True)
    title_type_name = serializers.CharField(read_only=True)
    release_format = ReleaseFormatSerializer(many=True)
    author = PersonSerializer(many=True)
    artist = PersonSerializer(many=True)
    publisher = PersonSerializer(many=True)

    class Meta:
        model = Title
        exclude = ['user', 'download_chapter', 'links_to_original', 'genres',
                   'tags', 'translators', 'description']


class TitleListSerializer(serializers.ModelSerializer):
    """ Serializer for manga-list """
    rate = TitleRatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=4, decimal_places=2)
    title_type_name = serializers.CharField(read_only=True)
    adult_content_name = serializers.CharField(read_only=True)
    author = PersonSerializer(many=True)
    genres = GenreSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Title
        fields = ['id', 'cover', 'russian_name', 'english_name', 'title_type',
                  'release_year', 'author', 'genres', 'tags', 'adult_content',
                  'description', 'rate', 'rating_count', '_average_rating', 'title_type_name',
                  'adult_content_name']


class TitleInfoSerializer(serializers.ModelSerializer):
    """ Serializer for info section TitleDetail """
    genres = GenreSerializer(many=True)
    tags = TagSerializer(many=True)
    translators = TranslatorsSerializer(many=True)
    similar_titles = SimilarSerializer(many=True)
    related_titles = RelatedSerializer(many=True)

    class Meta:
        model = Title
        fields = ['id', 'genres', 'tags', 'description', 'translators',
                  'similar_titles', 'related_titles']
