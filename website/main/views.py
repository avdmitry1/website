from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import About, Artist, Release
from django.views.decorators.cache import cache_page


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def releases_view(request: HttpRequest) -> HttpResponse:
    releases = Release.objects.select_related("artist").all()
    if not releases.exists():
        raise Http404("No releases found")
    return render(request, "main/releases.html", {"releases": releases})


def release_detail_view(request: HttpRequest, slug: str) -> HttpResponse:
    release = get_object_or_404(Release.objects.select_related("artist"), slug=slug)
    return render(request, "main/release_detail.html", {"release": release})


def artists_view(request: HttpRequest) -> HttpResponse:
    artists = Artist.objects.filter(is_active=True)
    return render(
        request, "main/artists.html", {"artists": artists, "no_artists": not artists}
    )


def artist_detail_view(request: HttpRequest, slug: str) -> HttpResponse:
    artist = get_object_or_404(
        Artist.objects.prefetch_related("releases", "social_links"),
        slug=slug,
    )
    return render(request, "main/artist_detail.html", {"artist": artist})


def events_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/events.html")


def podcast_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/podcast.html")


@cache_page(60 * 15)
def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/about.html", {"about": About.load()})
