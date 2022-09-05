from rest_framework import serializers

from info_section_app.models import SimilarTitle, SimilarLike, SimilarDislike, CRITERION_CHOICES, RelatedTitle, Folder, \
    Favorite
from title_app.models import Title


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


class FolderSerializer(serializers.ModelSerializer):
    """ Serializer for create folder """

    class Meta:
        model = Folder
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }


class FavoriteSerializer(serializers.ModelSerializer):
    liked = serializers.BooleanField(default=False)

    class Meta:
        model = Favorite
        fields = '__all__'

        extra_kwargs = {
            'user': {'read_only': True},
            'title': {'read_only': True}
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        fav_list = Favorite.objects.filter(title=instance.id).values_list('title_id', flat=True).first()
        if fav_list != None:
            response['liked'] = True
        return response
