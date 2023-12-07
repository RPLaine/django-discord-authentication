from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect
import requests

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=1181190931827916852&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&scope=identify"

def discord_login(request: HttpRequest):
    return redirect(auth_url_discord)

def discord_login_redirect(request: HttpRequest):
    if request.GET.get('code'):
        code = request.GET.get('code')
    else:
        code = "No code"

    user = exchange_code(code)

    return JsonResponse({
        'user': user,
        'code': code
        })

client_id = '1181190931827916852'
client_secret = 'cAb_hMZHAzu5WTv2OlIMIk9LHHeVZaLg'

def exchange_code(code: str):
    data = {
        'client_id': client_id, #This should be stored in an environment variable in production
        'client_secret': client_secret, #This should be stored in an environment variable in production
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/oauth2/login/redirect', #In production, this should be changed to the actual domain
        'scope': 'identify'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers) # the Token endpoint of Discord's OAuth2 provider
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/users/@me', headers={'Authorization': f'Bearer {access_token}'})
    user = response.json()
    return user