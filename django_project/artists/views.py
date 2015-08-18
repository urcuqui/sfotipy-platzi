from django.shortcuts import render
from .models import Artist
from django.views.generic.detail import DetailView
# Create your views here.

class ArtistDetailView(DetailView):
    model = Artist

    def get_template_names(self):
        return 'artist.html'
