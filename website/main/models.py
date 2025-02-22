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


# "--------------------------------------------------------------------------------------"


class Artist(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True, verbose_name="URL"
    )
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="artists/", blank=True, null=True)

    class Meta:
        indexes = [models.Index(fields=["name"], name="artist_name_idx")]
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Get the absolute URL for the artist.

        Returns the absolute URL for the artist, or raises a ValueError if the
        artist does not have a slug.

        """
        if not self.slug:
            raise ValueError("Artist must have a slug to get an absolute URL")
        return reverse("main:artist_page", args=[self.slug])


# "--------------------------------------------------------------------------------------"


class Release(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True, verbose_name="URL"
    )
    release_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to="releases/", blank=True, null=True)
    audio_file = models.FileField(upload_to="audio/", blank=True, null=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="releases"
    )

    class Meta:
        verbose_name = "Release"
        verbose_name_plural = "Releases"

    def __str__(self):
        return self.title


# "--------------------------------------------------------------------------------------"


class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("soundcloud", "SoundCloud"),
        ("other", "Other"),
    ]

    artist = models.ForeignKey(
        "Artist", on_delete=models.CASCADE, related_name="social_links", db_index=True
    )
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField(
        validators=[validators.URLValidator(schemes=["http", "https", "ftp"])]
    )

    class Meta:
        ordering = [models.functions.Lower("platform")]
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"

    def __str__(self):
        return f"{self.artist.name} - {self.platform}"


# "--------------------------------------------------------------------------------------"


class Event(BaseModel):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(db_index=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        indexes = [models.Index(fields=["date"], name="event_date_index")]
        ordering = ["date"]

    def __str__(self):
        return self.title

    @classmethod
    def upcoming_events(cls):
        """
        Get the upcoming events.

        Returns a queryset of events with a date greater than or equal to the
        current time, ordered by date.

        """
        return cls.objects.filter(date__gte=timezone.now()).order_by("date")


# "--------------------------------------------------------------------------------------"


class Podcast(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to="podcasts/", blank=True, null=True)
    link = models.URLField()

    class Meta:
        verbose_name = "Podcast"
        verbose_name_plural = "Podcasts"

    def __str__(self):
        return self.name


# "--------------------------------------------------------------------------------------"


class About(BaseModel):
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        About.objects.update_or_create(pk=1, defaults={"description": self.description})

    @classmethod
    def load(cls):
        return cls.objects.get_or_create(pk=1)[0]

    def __str__(self):
        return "About"
