from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
import requests
from django.shortcuts import render

auth_url_mpassid = "https://mpass-proxy-test.csc.fi/idp/profile/oidc/authorize?client_id=spa&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Fmpassid%2Flogin%2Fredirect&scope=openid"


def mpassid_login(request: HttpRequest):
    return render(request, 'mpassidlogin/index.html')

def mpassid_login_redirect(request: HttpRequest):
    if request.GET.get('code'):
        code = request.GET.get('code')
    else:
        code = "c2d748e9e453e42a80e8c45289da4642738d1af5" #This is a test code. In production, this should be handled differently

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
        'redirect_uri': 'http://localhost:8000/oauth2/mpassid/login/redirect', #In production, this should be changed to the actual domain
        'scope': 'openid profile'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('https://mpass-proxy-test.csc.fi/idp/profile/oidc/token', data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token', None]
    
    response = requests.get('https://mpass-proxy-test.csc.fi/idp/profile/oidc/userinfo', headers={'Authorization: Token c2d748e9e453e42a80e8c45289da4642738d1af5'})
    user = response.json()
    return user

def mpassid_login_probe(request: HttpRequest):
    return JsonResponse({
        'request': request.GET
    })