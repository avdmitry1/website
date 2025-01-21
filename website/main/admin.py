"""
Admin configuration for the main application

This module contains the admin configuration for the models in the main
application. It defines a custom admin class for the Artist model, which
customizes the admin interface for that model.
"""

from django.contrib import admin
from .models import Artist, Release, Event, Contact, About, SocialMediaLink


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inLines = [SocialMediaLink]
    list_display = ("name", "slug", "time_created")
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


class SocialMediaLink(admin.TabularInline):
    model = SocialMediaLink
    extra = 1


admin.site.register(Event)

admin.site.register(Contact)

admin.site.register(About)

# "----------------------------------------------------------------------------------------------------------"
