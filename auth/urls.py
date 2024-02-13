from django.urls import path

from auth.viewsets import LoginView

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(),
        name='api_token_auth'
    ),
]
