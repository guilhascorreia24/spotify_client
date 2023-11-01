import json
from django.http import JsonResponse
from django.shortcuts import render
import requests
import urlsAPI
import utilis
from . import models
from django.core import serializers


def Tracks(request):
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    print(urlsAPI.ENDPOINT_PLAYLISTS_USER(utilis.USER_ID))
    response = requests.get(urlsAPI.ENDPOINT_PLAYLISTS_USER(utilis.USER_ID), headers=headers)
    playlists = response.json()
    playlists=playlists["items"]
    context={"playlists":playlists}
    return render(request,'tracksInfo.html',context)

def Playlist(request,id):
    headers = {'Authorization': f'Bearer {request.session["access_token"]}'}
    response = requests.get(urlsAPI.ENDPOINT_LIST_PLAYLIST(id), headers=headers)
    playlist = response.json()
    
    # Create the playlist object
    #content = models.Playlist.objects.create(name=playlist['name'])

    # Iterate through the songs in the playlist and add them to the playlist
    content={}
    content['name']=playlist['name']
    content_songs=[]
    songs = playlist['tracks']['items']
    for song_data in songs:
        song = song_data['track']
        songv2=models.Song(
            title=song['name'],
            release_date=song['album']['release_date'],
            album=song['album']['name'],
            image_url=song['album']['images'][0]['url'],
            id=song['id']
            )
        songv2.set_artist(song['artists'])
        content_songs.append(songv2)
    serialize_json=serializers.serialize('json',content_songs)
    content_songs=json.loads(serialize_json)
    content['songs']=content_songs
    #content['access_token']=request.session['access_token']
    # Serialize the songs associated with the playlist
    #return JsonResponse(content, safe=False)
    return render(request,"ListPlaylist.html",{'playlist':content,'access_token':request.session['access_token']}); 