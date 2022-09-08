from django.urls import path
from info_section_app.views import SimilarView, SimilarDislikeView, SimilarLikeView, \
    RelatedView, FolderView, FavoriteView

urlpatterns = [
    path('<int:similar_pk>/like/', SimilarLikeView.as_view()),
    path('<int:similar_pk>/dislike/', SimilarDislikeView.as_view()),
    path('<int:title_pk>/similar', SimilarView.as_view({'post': 'create'})),
    path('<int:title_pk>/related', RelatedView.as_view({'post': 'create'})),
    path('folder/', FolderView.as_view({'post': 'create'})),
    path('<int:title_pk>/favorite/create', FavoriteView.as_view({'post': 'create'})),
    path('<int:title_pk>/favorite', FavoriteView.as_view({'get': 'list', 'delete': 'destroy'})),

    # path('<int:rest_pk>/review/create/', ReviewView.as_view({'get': 'list', 'post': 'create'})),
    # path('<int:rest_pk>/favorites/', FavoritesView.as_view()),
]
