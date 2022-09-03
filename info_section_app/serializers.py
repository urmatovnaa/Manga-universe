from rest_framework import serializers

from info_section_app.models import SimilarTitle, SimilarLike, SimilarDislike, CRITERION_CHOICES, RelatedTitle
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

    class Meta:
        model = Title
        fields = ['id', 'russian_name', 'cover']


class SimilarCreateSerializer(serializers.ModelSerializer):
    criterion = serializers.MultipleChoiceField(choices=CRITERION_CHOICES)

    class Meta:
        model = SimilarTitle
        fields = '__all__'
        extra_kwargs = {
            'main_title': {'read_only': True}
        }


class SimilarSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = RelatedTitle
        fields = '__all__'
        extra_kwargs = {
            'main_title': {'read_only': True}
        }


class RelatedSerializer(serializers.ModelSerializer):
    title = SimilarInfoSerializer()

    class Meta:
        model = RelatedTitle
        fields = '__all__'
