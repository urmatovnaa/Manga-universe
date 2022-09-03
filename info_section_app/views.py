from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from info_section_app.models import SimilarLike, SimilarDislike
from info_section_app.serializers import SimilarCreateSerializer, RelatedCreateSerializer


class SimilarView(ModelViewSet):
    """ View for create Similar Titles with exceptions """
    serializer_class = SimilarCreateSerializer
    lookup_field = 'title_pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            if request.data['title'] != str(kwargs.get('title_pk')):
                serializer.save(
                    main_title_id=kwargs.get('title_pk')
                )
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response('Нельзя добавить текущий тайтл в этот список')
        except Exception as e:
            print(e)
            return Response('Текущий тайтл есть в этом списке')


class SimilarLikeView(APIView):
    """ Like System """

    def get(self, request, similar_pk):
        created_liked = SimilarLike.objects.filter(similar_id=similar_pk, user=request.user).exists()
        created_disliked = SimilarDislike.objects.filter(similar_id=similar_pk, user=request.user).exists()
        if created_liked:
            SimilarLike.objects.filter(
                similar_id=similar_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            if created_disliked:
                SimilarDislike.objects.filter(
                    similar_id=similar_pk,
                    user=request.user
                ).delete()
            SimilarLike.objects.create(similar_id=similar_pk, user=request.user)
            return Response({'success': 'liked'})


class SimilarDislikeView(APIView):
    """ Dislike System """

    def get(self, request, similar_pk):
        created_liked = SimilarLike.objects.filter(similar_id=similar_pk, user=request.user).exists()
        created_disliked = SimilarDislike.objects.filter(similar_id=similar_pk, user=request.user).exists()
        if created_disliked:
            SimilarDislike.objects.filter(
                similar_id=similar_pk,
                user=request.user
            ).delete()
            return Response({'success': 'undisliked'})
        else:
            if created_liked:
                SimilarLike.objects.filter(
                    similar_id=similar_pk,
                    user=request.user
                ).delete()
            SimilarDislike.objects.create(similar_id=similar_pk, user=request.user)
            return Response({'success': 'disliked'})


class RelatedView(ModelViewSet):
    """ View for create Related Titles """
    serializer_class = RelatedCreateSerializer
    lookup_field = 'title_pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            if request.data['title'] != str(kwargs.get('title_pk')):
                serializer.save(
                    main_title_id=kwargs.get('title_pk')
                )
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response('Нельзя добавить текущий тайтл в этот список')
        except Exception as e:
            print(e)
            return Response('Текущий тайтл есть в этом списке')
