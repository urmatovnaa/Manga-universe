from django.urls import path
from apps.account_app.views import LoginView


urlpatterns = [
    # path('registration/', AccountRegisterAPIViews.as_view(), name='user-registration'),
    path('login/', LoginView.as_view())
]
