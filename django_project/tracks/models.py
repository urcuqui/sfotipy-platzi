from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_lenght=255)
    order = models.PositiveSmallIntegerField()
    track_file = models.FileField(upload_to='tracks')