from django.test import TestCase

from .models import Artist
from albums.models import Albums
from tracks.models import Track
# Create your tests here.
class TestArtist(TestCase):

    def setUp(self):
        self.artist = Artist.objects.create(name='david', last_name='bowie')
        self.album = Albums.objects.create(title='heroes', artist=self.artist)
        self.track = Track.objects.create(title='heroes', artist=self.artist, album=self.album, order=0, track_file='media/sa')

    def test_existe_vista(self):
        res = self.client.get('/artists/%d/' % self.artist.id)
        #200 status http que todo ocurrio perfecto
        self.assertEqual(res.status_code, 200)
        self.assertTrue('david' in res.content)

    def test_no_existe_vista(self):
        id_viejo = self.artist.id
        self.artist.delete()
        res = self.client.get('/artists/%d/' % id_viejo)
        #200 status http que todo ocurrio perfecto
        self.assertEqual(res.status_code, 404)

    def test_usuario_logeado(self):
        res = self.client.get('tracks/%s/' % self.track.title)
        self.assertEqual(res.status_code, 404)
