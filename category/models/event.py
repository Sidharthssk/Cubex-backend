from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


    class Meta:
        db_table = "event"
        verbose_name_plural = "Events"
        verbose_name = "Event"

    def __str__(self):
        return self.name


__all__ = ["Event", ]
