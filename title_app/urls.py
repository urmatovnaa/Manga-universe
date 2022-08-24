from django.urls import path, include
from title_app.views import TitleViewSet, MyUserRatingView

urlpatterns = [
    path('manga-list/', TitleViewSet.as_view({'get': 'list'})),
    path('<str:title_url>/', TitleViewSet.as_view(
        {'get': 'retrieve'}
    )),
    path('<int:tit_pk>/rating', MyUserRatingView.as_view({'post': 'create'})),
    # path('<int:rest_pk>/review/create/', ReviewView.as_view({'get': 'list', 'post': 'create'})),
    # path('<int:rest_pk>/favorites/', FavoritesView.as_view()),
]
