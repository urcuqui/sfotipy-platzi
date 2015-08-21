from django.shortcuts import render

# Create your views here.
from .models import Albums
from serializers import AlbumSerializer
from rest_framework import viewsets

class AlbumViewSet(viewsets.ModelViewSet):
    model = Albums
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer

