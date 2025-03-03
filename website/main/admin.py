"""
Admin configuration for the main application

This module contains the admin configuration for the models in the main
application. It defines a custom admin class for the Artist model, which
customizes the admin interface for that model.
"""

from django.contrib import admin
from .models import (
    Artist,
    Genre,
    Release,
    Event,
    Podcast,
    About,
    SocialMediaLink,
    Track,
)
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.db import models


class CustomTextWidget(WysiwygWidget):
    def __init__(self, attrs=None):
        default_attrs = {
            "style": "background-color: #f0f0f0; color: #333; font-size: 14px; padding: 10px;",
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1


@admin.register(Artist)
class ArtistAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CustomTextWidget()},
    }
    inlines = [SocialMediaLinkInline]
    list_display = ("name", "slug", "time_created")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")

    def view_on_site(self, obj):
        return obj.get_absolute_url()

    view_on_site.short_description = "View on Site"


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Track)
class Track(ModelAdmin):
    list_display = ("name", "track_number", "release")
    search_fields = ("name", "release__title")
    ordering = ("track_number",)



@admin.register(Release)
class ReleaseAdmin(ModelAdmin):
    search_fields = ("title", "artists__name")
    list_display = ("title", "slug", "get_artists", "release_date", "time_created")
    list_filtered = ("release_date", "genres")
    ordering = ("release_date",)
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {
        models.TextField: {"widget": CustomTextWidget()},
    }

    def get_artists(self, obj):
        return ", ".join([artist.name for artist in obj.artists.all()])

    get_artists.short_description = "Artists"


@admin.register(Event)
class EventAdmin(ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "time_created", "date", "location", "event_url")
    ordering = ("date",)
    formfield_overrides = {
        models.TextField: {"widget": CustomTextWidget()},
    }


@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ("description", "time_created")
    formfield_overrides = {
        models.TextField: {"widget": CustomTextWidget()},
    }


@admin.register(Podcast)
class PodcastAdmin(ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "link", "time_created")
    formfield_overrides = {
        models.TextField: {"widget": CustomTextWidget()},
    }


# "----------------------------------------------------------------------------------------------------------"
