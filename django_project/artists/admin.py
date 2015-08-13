from django.contrib import admin

# Register your models here.
from .models import Artist

from tracks.models import Track
from albums.models import Albums

class AlbumInLine(admin.StackedInline):
    model = Albums

class TrackInLine(admin.StackedInline):
    model = Track

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('name', 'last_name')
    inlines = [TrackInLine, AlbumInLine]
    filter_horizontal = ('favorite_songs',)



admin.site.register(Artist, ArtistAdmin)