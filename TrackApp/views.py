from django.shortcuts import render
import requests
import urlsAPI
import utilis


def Profile(request):
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    print(urlsAPI.ENDPOINT_PLAYLISTS_USER(utilis.USER_ID))
    response = requests.get(urlsAPI.ENDPOINT_PLAYLISTS_USER(utilis.USER_ID), headers=headers)
    playlists = response.json()
    playlists=playlists["items"]
    print(playlists)
    context={"playlists":playlists}
    return render(request,'tracksInfo.html',context)