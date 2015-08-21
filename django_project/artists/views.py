from django.shortcuts import render
from .models import Artist
from django.views.generic.detail import DetailView
from django.views.generic import ListView
# Create your views here.

class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'
    template_name = 'artist.html'

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artists'
    def get_template_names(self):
        return 'artist.html'

from rest_framework import viewsets
from .serializers import ArtistSerializer
class ArtistViewSet(viewsets.ModelViewSet):
    model = Artist
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    filter_fields =('id')
    paginate_by = 1
