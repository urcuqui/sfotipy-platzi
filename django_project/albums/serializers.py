from rest_framework import serializers
from .models import Albums
class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums