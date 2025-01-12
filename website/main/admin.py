from django.contrib import admin
from .models import Artist, Release, Event, Contact, About


admin.site.register(Artist)
admin.site.register(Release)
admin.site.register(Event)
admin.site.register(Contact)
admin.site.register(About)