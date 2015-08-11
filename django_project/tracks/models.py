from django.db import models

from albums.models import Albums
from artists.models import Artist


class Track(models.Model):
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    album = models.ForeignKey(Albums)
    artist = models.ForeignKey(Artist)

    def __unicode__(self):
            return self.title
