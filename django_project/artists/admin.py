from django.contrib import admin

# Register your models here.
from .models import Artist

from tracks.models import Track

class TrackInLine(admin.StackedInline):
    model = Track

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('name', 'last_name')
    inlines = [TrackInLine]



admin.site.register(Artist, ArtistAdmin)