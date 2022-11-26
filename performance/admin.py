from django.contrib import admin
from .models import Performance
from category.models import AgeGroup
from django.contrib.admin import SimpleListFilter


class AgeGroupFilter(SimpleListFilter):
    title = 'Age Group'  # or use _('country') for translated title
    parameter_name = 'ageGroup'

    def lookups(self, request, model_admin):
        return [(a.id, a.name) for a in AgeGroup.objects.all()]

    def queryset(self, request, queryset):
        if self and self.value():
            return queryset.filter(participant__ageGroup=self.value())
        return queryset


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("get_rank", "participant", "event", "age_group", "duration",)
    search_fields = ("participant__name", "event__name")
    exclude = ['timeStampCreated', ]
    autocomplete_fields = ['event', 'participant']
    list_filter = ["event", AgeGroupFilter]

    def age_group(self, obj):
        return obj.participant.ageGroup

    def get_rank(self, obj):
        return Performance.objects.filter(
            event=obj.event,
            participant__ageGroup=obj.participant.ageGroup
        ).filter(duration__lt=obj.duration).count() + 1

    get_rank.short_description = 'Rank'
    age_group.short_description = 'Age Group'

