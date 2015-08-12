from django.contrib import admin

# Register your models here.
from .models import Track

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'order', 'track_file','album')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__name', 'artist__last_name')

admin.site.register(Track, TrackAdmin)