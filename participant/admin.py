from django.contrib import admin
from .models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "email", "dob", "isOnline", "ageGroup")
    search_fields = ("name", "email", "contact")
    list_filter = ['ageGroup', "isOnline", "events"]
    autocomplete_fields = ['ageGroup', 'events']

