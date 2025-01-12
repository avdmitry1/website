from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("releases/", views.releases, name="releases"),
    path("artists/", views.artists, name="artists"),
    path("events/", views.events, name="events"),
    path("contacts/", views.contacts, name="contacts"),
    path("about/", views.about, name="about"),
]
