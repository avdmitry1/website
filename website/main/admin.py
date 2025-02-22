"""
Admin configuration for the main application

This module contains the admin configuration for the models in the main
application. It defines a custom admin class for the Artist model, which
customizes the admin interface for that model.
"""

from django.contrib import admin
from .models import Artist, Release, Event, Podcast, About, SocialMediaLink
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from django.db import models


class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1


@admin.register(Artist)
class ArtistAdmin(ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    inlines = [SocialMediaLinkInline]
    list_display = ("name", "slug", "time_created")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")

    def view_on_site(self, obj):
        return obj.get_absolute_url()

    view_on_site.short_description = "View on Site"


@admin.register(Release)
class ReleaseAdmin(ModelAdmin):
    search_fields = ("title", "artist")
    list_display = ("title", "slug", "artist", "release_date", "time_created")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Event)
admin.site.register(About)


@admin.register(Podcast)
class PodcastAdmin(ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "link", "time_created")


# "----------------------------------------------------------------------------------------------------------"
