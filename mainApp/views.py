import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
import requests
from AuthenticationAPP.views import spotify_login
import urlsAPI
# Create your views here.
def home(request):
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    response = requests.get(urlsAPI.URL_ME, headers=headers)
    user_data = response.json()
    print(user_data)
    data={"user":user_data}
    return JsonResponse(data)

def login_logout(request):
    return redirect("login")