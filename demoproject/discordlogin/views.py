from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=1181190931827916852&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&scope=identify"

def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'message': 'Hello, world!'})

def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)

def discord_login_redirect(request: HttpRequest):
    return JsonResponse({'message': 'Redirected!'})