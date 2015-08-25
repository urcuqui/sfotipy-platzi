from django.contrib import admin

# Register your models here.
from .models import Albums
from sorl.thumbnail import get_thumbnail


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_album')

    def image_album(self, obj):
        return '<img src="%s">' % get_thumbnail(obj.cover, '100x100', crap='center').url

    image_album.allow_tags = True


admin.site.register(Albums, AlbumAdmin)
