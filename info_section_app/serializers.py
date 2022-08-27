from django.db.models import Count
from rest_framework import serializers

from info_section_app.models import SimilarTitle


class SimilarSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimilarTitle
        fields = '__all__'
        extra_kwargs = {
            'main_title': {'read_only': True},
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['similar_count'] = 'likes'.count()

        return representation
