from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_lenght=255)
    order = models.PositiveSmallIntegerField()
    track_file = models.FileField(upload_to='tracks')

class Artist(models.Model):
    name = models.CharField(max_length=255)
    biography = models.CharField(max_length=255)

class Gender(models.Model):
    name = models.CharField(max_length=255)

class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='albums')


