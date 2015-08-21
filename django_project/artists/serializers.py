from rest_framework import serializers
from .models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    es_pharrel = serializers.SerializerMethodField('es_pharrel')

    def es_pharrel(self, obj):
        return obj.es_pharrel()

    class Meta:
        model = Artist
        fields = ('id', 'name', 'last_name', 'es_pharrel')
