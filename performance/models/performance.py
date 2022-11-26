from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
from participant.models import Participant
from category.models import Event


class Performance(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    duration = models.DurationField(default=timedelta(minutes=0, milliseconds=0), help_text='format: hh:mm:ss.ms')
    timeStampCreated = models.DateTimeField(default=timezone.now)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    @property
    def ageGroup(self):
        return self.participant.ageGroup

    class Meta:
        ordering = ['duration']
        unique_together = [
            ('participant', 'event')
        ]
        db_table = "performance"
        verbose_name_plural = "Performances"
        verbose_name = "Performance"

    def __str__(self):
        return str(self.id)


__all__ = ["Performance", ]
