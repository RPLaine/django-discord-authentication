from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

def index(request: HttpRequest) -> HttpResponse:
    return JsonResponse({'message': 'Hello, world!'})