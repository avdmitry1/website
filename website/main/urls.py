from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name: str = "main"

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
    path("releases/", views.releases, name="releases"),
    path("artists/", views.artists_view_all, name="artists_all"),
    path("artists/<slug:slug>/", views.artist_person_page, name="artist_person_page"),
    path("events/", views.events, name="events"),
    path("contacts/", views.contacts, name="contacts"),
    path("about/", views.about, name="about"),
]

