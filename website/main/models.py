from django.db import models
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    photo = models.ImageField(upload_to="artists/")
    social_links = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Release(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to="releases/")
    audio_file = models.FileField(upload_to="audio/")
    streaming_links = models.JSONField(default=dict)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class About(models.Model):
    history = models.TextField()
    description = models.TextField()

    def __str__(self):
        return "About us"
