import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Track


# Create your views here.
@login_required
def track_view(request, title):
    # try:
    #    track = Track.object.get(title=title)
    # except Track.DoesNotExist:
    #    return Http404
    #import ipdb; ipdb.set_trace()
    track = get_object_or_404(Track, title=title)
    bio = track.artist.biography

    data = {
        'title': track.title,
        'order': track.order,
        'album': track.album.title,
        'artist': {
            'name': track.artist.name,
            'bio': bio,
        }
    }
    json_data = json.dumps(data)
    #return HttpResponse(json_data, content_type='application/json')
    return render(request, 'track.html', {'track': track})
