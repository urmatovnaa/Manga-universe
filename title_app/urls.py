from django.urls import path
from title_app.views import TitleViewSet, MyUserRatingView, TitleInfoViewSet
from info_section_app.views import SimilarView, SimilarDislikeView, SimilarLikeView

urlpatterns = [
    path('manga-list/', TitleViewSet.as_view({'get': 'list'})),
    path('<str:title_url>/', TitleViewSet.as_view(
        {'get': 'retrieve'}
    )),
    path('<str:title_url>/info', TitleInfoViewSet.as_view({'get': 'retrieve'})),
    path('<int:title_pk>/rating/create', MyUserRatingView.as_view({'post': 'create'})),
    path('<int:title_pk>/rating', MyUserRatingView.as_view({'get': 'list'})),

    # path('<int:rest_pk>/review/create/', ReviewView.as_view({'get': 'list', 'post': 'create'})),
    # path('<int:rest_pk>/favorites/', FavoritesView.as_view()),
]
