from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "main/index.html")


def releases(request):
    return render(request, "main/releases.html")


def artists(request):
    return render(request, "main/artists.html")


def events(request):
    return render(request, "main/events.html")


def contacts(request):
    return render(request, "main/contacts.html")


def about(request):
    return render(request, "main/about.html")
