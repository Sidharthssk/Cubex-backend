from django.contrib import admin
from .models import AgeGroup, Event


@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "minAge", "maxAge")
    search_fields = ("name", "event")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


