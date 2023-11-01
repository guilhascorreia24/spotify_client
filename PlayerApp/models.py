from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='music_images/')
    audio_file = models.FileField(upload_to='music_files/')