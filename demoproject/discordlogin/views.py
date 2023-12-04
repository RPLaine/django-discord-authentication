from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'message': 'Hello, world!'})

def discord_login(request: HttpRequest) -> HttpResponse:
    return render(request, 'discordlogin/discord-login.html')