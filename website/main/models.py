from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    time_created = models.DateTimeField(default=now)
    time_updated = models.DateTimeField(default=now)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# "----------------------------------------------------------------------------------------------------------"


class Artist(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True, verbose_name="URL"
    )
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="artists/", blank=True, null=True)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name

# "----------------------------------------------------------------------------------------------------------"


class Release(BaseModel):
    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(
        max_length=50, unique=True, db_index=True, verbose_name="URL"
    )
    release_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(
        upload_to="releases/", blank=True, null=True)
    audio_file = models.FileField(upload_to="audio/", blank=True, null=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="releases"
    )

    class Meta:
        verbose_name = "Release"
        verbose_name_plural = "Releases"

    def __str__(self):
        return self.title

# "----------------------------------------------------------------------------------------------------------"


class SocialMediaLink(models.Model):
    PLATFORM_CHOICES = [
        ("instagram", "Instagram"),
        ("soundcloud", "SoundCloud"),
        ("other", "Other"),
    ]

    artist = models.ForeignKey(
        "Artist", on_delete=models.CASCADE, related_name="social_links"
    )
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()

    class Meta:
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"

    def __str__(self):
        return f"{self.artist.name} - {self.platform}"

# "----------------------------------------------------------------------------------------------------------"


class Event(BaseModel):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email


class About(models.Model):
    description = models.TextField(blank=True)

    def __str__(self):
        return "About"

# "----------------------------------------------------------------------------------------------------------"
