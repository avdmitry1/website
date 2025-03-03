from datetime import timezone
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import About, Artist, Genre, Release, Track, Event, Podcast
from django.views.decorators.cache import cache_page


def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/index.html")


def releases_view(request: HttpRequest) -> HttpResponse:
    releases = Release.objects.prefetch_related("artists", "genres").all()
    return render(request, "main/releases.html", {"releases": releases})


def filtered_releases_view(request: HttpRequest) -> HttpResponse:
    releases = Release.objects.prefetch_related("artists", "genres").all()

    # filter by artist
    artist_slug = request.GET.get("artist")
    if artist_slug:
        releases = releases.filter(artists__slug=artist_slug)

    # filter by genre
    genre_slug = request.GET.get("genre")
    if genre_slug:
        releases = releases.filter(genres__slug=genre_slug)

    # filter by year
    year = request.GET.get("year")
    if year and year.isdigit():
        releases = releases.filter(release_date__year=int(year))

    # Sort
    sort = request.GET.get("sort", "-release_date")  # Default new first
    releases = releases.order_by(sort)

    return render(request, "main/filtered_releases.html", {"releases": releases})


def release_detail_view(request: HttpRequest, slug: str) -> HttpResponse:
    release = get_object_or_404(
        Release.objects.prefetch_related("artist", "tracks", "genres"), slug=slug
    )
    return render(request, "main/release_detail.html", {"release": release})


def track_detail_view(
    request: HttpRequest,
    release_slug: str,
    track_number: int,
) -> HttpResponse:
    track = get_object_or_404(
        Track.objects.select_related("release").prefetch_related("release__artists"),
        release__slug=release_slug,
        track_number=track_number,
    )
    return render(request, "main/track_detail.html", {"track": track})


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
    upcoming_events = Event.upcoming_events().prefetch_related("artists")
    past_events = (
        Event.objects.filter(date__lt=timezone.now(), is_active=True)
        .prefetch_related("artists")
        .order_by("-date")[:10]
    )

    return render(
        request,
        "main/events.html",
        {"upcoming_events": upcoming_events, "past_events": past_events},
    )


def event_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    event = get_object_or_404(Event.objects.prefetch_related("artists"), pk=pk)
    return render(request, "main/event_detail.html", {"event": event})


def podcast_view(request: HttpRequest) -> HttpResponse:
    podcasts = Podcast.objects.filter(is_active=True).order_by("-date")
    return render(request, "main/podcast.html", {"podcasts": podcasts})


@cache_page(60 * 15)
def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/about.html", {"about": About.load()})
