from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Artist


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def releases(request: HttpRequest) -> HttpResponse:
    return render(request, "main/releases.html")

# "----------------------------------------------------------------------------------------------------------"


def artists_view_all(request: HttpRequest) -> HttpResponse:
    """Render the artists page with a list of all artists."""
    artists = Artist.objects.all()
    context: Dict[str, Any] = {'artists': artists}
    return render(request, "main/artists.html", context)


def artist_person_page(request: HttpRequest, slug: str) -> HttpResponse:
    """Render the artist detail page for a specific artist identified by slug."""
    artist = get_object_or_404(Artist, slug=slug)
    context: Dict[str, Any] = {'artist': artist}
    return render(request, 'main/artist_detail.html', context)

# "----------------------------------------------------------------------------------------------------------"


def events(request: HttpRequest) -> HttpResponse:
    return render(request, "main/events.html")


def contacts(request: HttpRequest) -> HttpResponse:
    return render(request, "main/contacts.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "main/about.html")
