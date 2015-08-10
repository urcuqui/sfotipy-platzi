from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    biography = models.CharField(blank=True)