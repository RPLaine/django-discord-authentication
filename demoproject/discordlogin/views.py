from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import requests
from .models import *
from django.core import serializers
import json

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=1181190931827916852&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Fdiscord%2Flogin%2Fredirect&scope=identify"


def discord_login(request: HttpRequest):
    return render(request, 'discordlogin/index.html')

def discord_login_redirect(request: HttpRequest):
    if request.GET.get('code'):
        code = request.GET.get('code')
    else:
        code = "No code"

    user = exchange_code(code)

    return access(request, user)

client_id = '1181190931827916852'
client_secret = 'cAb_hMZHAzu5WTv2OlIMIk9LHHeVZaLg'

def exchange_code(code: str):
    data = {
        'client_id': client_id, #This should be stored in an environment variable in production
        'client_secret': client_secret, #This should be stored in an environment variable in production
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8000/oauth2/discord/login/redirect', #In production, this should be changed to the actual domain
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

def access(request: HttpRequest, user: dict):
    context = {}

    # Test if the user exists in the database
    user_data = UserData.objects.filter(discord_id=user['id'])
    if user_data.exists():
        context["database_message"] = "User found in UserData table!"
    else:
        context["database_message"] = "User not found in UserData table. Creating a new entry."

        #If the user does not exist in the database, create a new entry
        UserData.objects.create(
            discord_id = user['id'],
            username = user['username'],
            avatar = user['avatar'],
            discriminator = user['discriminator'],
            public_flags = user['public_flags'],
            premium_type = user['premium_type'],
            flags = user['flags'],
            banner = user['banner'],
            accent_color = user['accent_color'],
            global_name = user['locale'],
            avatar_decoration_data = user['avatar_decoration_data'],
            banner_color = user['banner_color'],
            mfa_enabled = user['mfa_enabled'],
            locale = user['locale']
        )
        user_data = UserData.objects.filter(discord_id=user['id'])

    #Transforms the user_data object into a JSON object and then into a Python dictionary
    user_data_json = serializers.serialize('json', user_data)
    user_data_json = json.loads(user_data_json)
    fields_dict = user_data_json[0]['fields']

    context["user"] = fields_dict

    #Check if the user has a nmid
    if fields_dict['nmid'] is None:
        context["nmid_message"] = "No nmid found in database."
    else:
        context["nmid_message"] = "nmid found in database."
    
    return render(request, 'discordlogin/access.html', context)