from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, custom_login

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', custom_login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
