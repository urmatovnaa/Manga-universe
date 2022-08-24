from django.db.models import Count, F, Avg
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from rest_framework.response import Response

from title_app.models import Title, Rating
from title_app.serializers import TitleListSerializer, TitleRatingSerializer, TitleDetailSerializer
from title_app.pagination import TitlesPagination
from title_app.filters import TitleFilter
from title_app.permissions import RatingPermission


class TitleViewSet(viewsets.ModelViewSet):
    """ Каталог Манги """
    # queryset = Title.objects.all().order_by('-rating_count')
    serializer_class = TitleListSerializer
    serializer_classes = {
        'retrieve': TitleDetailSerializer,
    }
    lookup_field = 'title_url'
    pagination_class = TitlesPagination
    filterset_class = TitleFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['russian_name', 'english_name', 'alternative_names']
    ordering_fields = ['rating_count', 'english_name', 'date_created']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Title.objects.all().annotate(rating_count=Count('rate__star'),
                                            _average_rating=Avg('rate__star')).order_by('-rating_count')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyUserRatingView(viewsets.ModelViewSet):
    serializer_class = TitleRatingSerializer
    permission_classes = (RatingPermission, )
    queryset = Rating.objects.all()
    lookup_field = 'tit_pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            title=kwargs.get('tit_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)




