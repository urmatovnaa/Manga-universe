from rest_framework import serializers

from apps.info_section_app.models import SimilarTitle, SimilarLike, SimilarDislike, CRITERION_CHOICES, \
    RelatedTitle, Favorite
from apps.title_app.models import Title


class SimilarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarLike
        fields = '__all__'


class SimilarDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarDislike
        fields = '__all__'


class SimilarInfoSerializer(serializers.ModelSerializer):
    """ Serializer for get info about related/similar title """

    class Meta:
        model = Title
        fields = ['id', 'russian_name', 'cover']


class SimilarCreateSerializer(serializers.ModelSerializer):
    """ Serializer for create Similar Titles """
    criterion = serializers.MultipleChoiceField(choices=CRITERION_CHOICES)

    class Meta:
        model = SimilarTitle
        fields = '__all__'
        extra_kwargs = {
            'main_title': {'read_only': True}
        }


class SimilarSerializer(serializers.ModelSerializer):
    """ Serializer for get Similar Titles with similar count """
    likes = SimilarLikeSerializer(many=True)
    dislikes = SimilarDislikeSerializer(many=True)
    title = SimilarInfoSerializer()

    class Meta:
        model = SimilarTitle
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['similar_count'] = len(response['likes'])-len(response['dislikes'])
        return response


class RelatedCreateSerializer(serializers.ModelSerializer):
    """ Serializer for create Related Titles """

    class Meta:
        model = RelatedTitle
        fields = '__all__'
        extra_kwargs = {
            'main_title': {'read_only': True},
            'user': {'read_only': True}
        }


class RelatedSerializer(serializers.ModelSerializer):
    """ Serializer for get Related Titles """
    title = SimilarInfoSerializer()

    class Meta:
        model = RelatedTitle
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    """ Serializer for adding tittles to the folder """

    class Meta:
        model = Favorite
        fields = '__all__'

        extra_kwargs = {
            'user': {'read_only': True},
            'title': {'read_only': True}
        }

    def create(self, validated_data):
        manga_list, _ = Favorite.objects.update_or_create(
            user=validated_data.get('user', None),
            title_id=validated_data.get('title', None),
            defaults={'folder': validated_data.get("folder")}
        )
        return manga_list

