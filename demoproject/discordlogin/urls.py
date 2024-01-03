from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda req: redirect("login/")),
    path('login/', views.discord_login, name='discord_login'),
    path('login/redirect', views.discord_login_redirect, name='discord_login_redirect'),
    path('access/', views.access, name='access'),
]