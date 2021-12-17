from django import views
from django.shortcuts import render

from .models import Artist, Album

class BaseView(views.View):
    """Базовое представление"""

    def get(self, request, *args, **kwargs):
        return render(request, "base.html", {})


class ArtistDetailView(views.generic.DetailView):
    """Детализированное представление исполнителя"""

    model = Artist
    template_name = 'artist/artist_detail.html'
    slug_url_kwarg = 'artist_slug'
    context_object_name = 'artist'


class AlbumDetailView(views.generic.DetailView):
    """Детализированное представление исполнителя"""

    model = Album
    template_name = 'album/artist_detail.html'
    slug_url_kwarg = 'album_slug'
    context_object_name = 'album'
