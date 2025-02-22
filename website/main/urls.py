from django.urls import path
from . import views

app_name: str = "main"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("releases/", views.releases_view, name="releases"),
    path("artists/", views.artists_view, name="artists"),
    path("artists/<slug:slug>/", views.artist_detail_view, name="artist_page"),
    path("events/", views.events_view, name="events"),
    path("podcast/", views.podcast_view, name="podcast"),
    path("about/", views.about_view, name="about"),
]

