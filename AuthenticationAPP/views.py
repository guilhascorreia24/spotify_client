

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import requests
from social_django.utils import psa
from spotipy.oauth2 import SpotifyOAuth
import credentials
import utilis
import urlsAPI



def spotify_login(request):
    sp_oauth = SpotifyOAuth(client_id=credentials.client_ID, client_secret=credentials.client_SECRET, redirect_uri=credentials.redirect_URI, scope = credentials.scope)
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return HttpResponseRedirect(auth_url)

def spotify_logout(request):
    request.session.flush()
    return redirect('home')

def callback(request):

    print("callback")
    sp_oauth = SpotifyOAuth(client_id=credentials.client_ID, client_secret=credentials.client_SECRET, redirect_uri=credentials.redirect_URI, scope = credentials.scope)
    print(request)
    code = request.GET.get("code")
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info["access_token"]
    request.session["access_token"] = access_token
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    response = requests.get(urlsAPI.URL_ME, headers=headers)
    user_data = response.json()
    print(user_data)
    utilis.USER_ID=user_data["id"]
    return redirect('home')
