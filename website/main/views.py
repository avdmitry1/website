from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "main/index.html")


def releases(request):
    return render(request, "main/releases.html")


def artists(request):
    return render(request, "main/artists.html")


def artists_view(request):
    artists = [
        {"name": "Artist 1", "image": "img/font1.png"},
        {"name": "Artist 2", "image": "img/font2.png"},
        {"name": "Artist 3", "image": "img/font3.png"},
        {"name": "Artist 4", "image": "img/font4.png"},
        {"name": "Artist 5", "image": "img/font5.png"},
        {"name": "Artist 6", "image": "img/font6.png"},
        {"name": "Artist 3", "image": "img/font3.png"},
        {"name": "Artist 6", "image": "img/font6.png"},
        {"name": "Artist 4", "image": "img/font4.png"},
        {"name": "Artist 5", "image": "img/font5.png"},
        {"name": "Artist 6", "image": "img/font6.png"},
        {"name": "Artist 3", "image": "img/font3.png"},
        {"name": "Artist 6", "image": "img/font6.png"},
        
    ]
    return render(request, "main/artists.html", {"artists": artists})


def events(request):
    return render(request, "main/events.html")


def contacts(request):
    return render(request, "main/contacts.html")


def about(request):
    return render(request, "main/about.html")
