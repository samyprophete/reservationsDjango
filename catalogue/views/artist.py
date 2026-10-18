from django.shortcuts import render
from django.http import Http404
from catalogue.models import Artist

def index(request):
    """Affiche la liste complete des artistes (Browse / Index)."""
    artists = Artist.objects.all()
    return render(request, 'artist/index.html', {
        'artists' : artists,
        'title' : 'Liste des artistes',
    })

def show(request, artist_id):
    """Affiche la fiche detaillée d'un artiste ou une 404 s'il n'existe pas."""
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404("L'artiste inexistant")
    return render(request, 'artist/show.html', {
        'artist' : artist,
    })