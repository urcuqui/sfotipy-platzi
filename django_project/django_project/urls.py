from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from artists.views import ArtistDetailView, ArtistListView, ArtistViewSet
from rest_framework import viewsets, routers

router = routers.DefaultRouter()
router.register(r'artists', ArtistViewSet)

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'django_project.tracks.views', name='hola'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-W]+)/', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)), # admin site
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),
    url(r'^api', include(router.urls)),
)
#Tener en cuenta que solo se habilita cuando esta en el entorno de desarrollo
urlpatterns += patterns ('',
           url (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),
                         )