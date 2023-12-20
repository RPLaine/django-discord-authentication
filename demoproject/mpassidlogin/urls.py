from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda req: redirect("login/")),
    path('login/', views.mpassid_login, name='mpassid_login'),
    path('login/redirect', views.mpassid_login_redirect, name='mpassid_login_redirect'),
    path('loginprobe/', views.mpassid_login_probe, name='mpassid_login_probe'),
]