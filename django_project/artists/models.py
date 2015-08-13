from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    biography = models.TextField(blank=True)
    favorite_songs = models.ManyToManyField('tracks.Track', blank=True, related_name='is_favorite_of')

    def __unicode__(self):
        return self.name