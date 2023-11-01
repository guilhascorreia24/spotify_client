from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    artists = models.CharField(max_length=100)
    id=models.CharField(max_length=100,primary_key=True)
    #genre = models.CharField(max_length=50)
    release_date = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    image_url=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def set_artist(self,artists):
        #print(artists)
        #print("artists:")
        self.artists=artists[0]['name']
        for artist in artists[1:]:
            #print(artist['name'])
            self.artists+=","+artist['name']
        

    def get_artists(self):
        return self.artists