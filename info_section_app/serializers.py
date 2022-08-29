from rest_framework import serializers

from info_section_app.models import SimilarTitle, SimilarLike, SimilarDislike


class SimilarLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarLike
        fields = '__all__'


class SimilarDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarDislike
        fields = '__all__'


class SimilarSerializer(serializers.ModelSerializer):
    likes = SimilarLikeSerializer(many=True)
    dislikes = SimilarDislikeSerializer(many=True)

    class Meta:
        model = SimilarTitle
        fields = '__all__'
        extra_kwargs = {
            'main_title': {'read_only': True},
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['similar_count'] = len(response['likes'])-len(response['dislikes'])
        return response

