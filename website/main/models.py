from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core import validators


class BaseModel(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Artist(BaseModel):
    name = models.CharField(
        max_length=50,
        db_index=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="URL",
    )
    bio = models.TextField(blank=True)
    photo = models.ImageField(
        upload_to="artists/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:artist_page", args=[self.slug])


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Release(BaseModel):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="URL",
    )
    release_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to="releases/", blank=True, null=True)
    audio_file = models.FileField(
        upload_to="audio/",
        blank=True,
        null=True,
    )
    description = models.TextField(blank=True)
    artists = models.ManyToManyField(Artist, related_name="releases")
    genres = models.ManyToManyField(Genre, related_name="releases", blank=True)

    class Meta:
        verbose_name = "Release"
        verbose_name_plural = "Releases"

    def __str__(self):
        return self.title


class Track(BaseModel):
    name = models.CharField(max_length=100, db_index=True)
    release = models.ForeignKey(
        Release,
        on_delete=models.CASCADE,
        related_name="tracks",
    )
    track_number = models.PositiveSmallIntegerField()
    bpm = models.PositiveSmallIntegerField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name="tracks", blank=True)
    audio_preview = models.FileField(
        upload_to="audio/previews/",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["track_number"]
        verbose_name = "Track"
        verbose_name_plural = "Tracks"

    def __str__(self):
        return f"{self.name} - {self.track_number}"


class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("soundcloud", "SoundCloud"),
        ("bandcamp", "Bandcamp"),
        ("spotify", "Spotify"),
        ("facebook", "Facebook"),
        ("twitter", "Twitter"),
        ("youtube", "YouTube"),
        ("beatport", "Beatport"),
        ("mixcloud", "Mixcloud"),
        ("other", "Other"),
    ]

    artist = models.ForeignKey(
        "Artist",
        on_delete=models.CASCADE,
        related_name="social_links",
        db_index=True,
    )
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField(
        validators=[
            validators.URLValidator(schemes=["http", "https"]),
        ]
    )

    class Meta:
        ordering = [models.functions.Lower("platform")]
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"

    def __str__(self):
        return f"{self.artist.name} - {self.platform}"


class Event(BaseModel):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, db_index=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    event_url = models.URLField(
        validators=[
            validators.URLValidator(schemes=["http", "https"]),
        ]
    )
    artists = models.ManyToManyField(Artist, related_name="events", blank=True)
    image = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name

    @classmethod
    def upcoming_events(cls):
        """
        Get the upcoming events.

        Returns a queryset of events with a date greater than or equal to the
        current time, ordered by date.

        """
        return cls.objects.filter(date__gte=timezone.now()).order_by("date")


class Podcast(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    audio_file = models.FileField(
        upload_to="podcasts/",
        blank=True,
        null=True,
    )
    link = models.URLField(
        validators=[
            validators.URLValidator(schemes=["http", "https"]),
        ]
    )
    date = models.DateField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = "Podcast"
        verbose_name_plural = "Podcasts"

    def __str__(self):
        return f"{self.name} - {self.date.strftime('%d.%m.%Y')}"


class About(BaseModel):
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "About"

    def __str__(self):
        return "About"
