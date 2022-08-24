from rest_framework import serializers

from title_app.models import Title, Rating


class TitleRatingSerializer(serializers.ModelSerializer):

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
            title=validated_data.get('title', None),
            defaults={'star': validated_data.get("star")}
        )
        return rate


class TitleDetailSerializer(serializers.ModelSerializer):
    rate = TitleRatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=4, decimal_places=2)
    title_status_name = serializers.CharField(read_only=True)
    translator_status_name = serializers.CharField(read_only=True)
    adult_content_name = serializers.CharField(read_only=True)
    title_type_name = serializers.CharField(read_only=True)

    class Meta:
        model = Title
        exclude = ['user', 'download_chapter', 'links_to_original', 'genres',
                   'tags', 'translators', 'description']


class TitleListSerializer(serializers.ModelSerializer):
    rate = TitleRatingSerializer(many=True)
    rating_count = serializers.IntegerField(read_only=True)
    _average_rating = serializers.DecimalField(read_only=True, max_digits=4, decimal_places=2)
    title_type_name = serializers.CharField(read_only=True)
    adult_content_name = serializers.CharField(read_only=True)

    class Meta:
        model = Title
        fields = ['id', 'cover', 'russian_name', 'english_name', 'title_type',
                  'release_year', 'author', 'genres', 'tags', 'adult_content',
                  'description', 'rate', 'rating_count', '_average_rating', 'title_type_name',
                  'adult_content_name']

