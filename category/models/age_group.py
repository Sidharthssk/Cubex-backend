from django.db import models
from .event import Event


class AgeGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    minAge = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    maxAge = models.PositiveSmallIntegerField(default=12, null=True, blank=True)
    event = models.ManyToManyField(Event)

    class Meta:
        db_table = "age_group"
        verbose_name_plural = "Age Groups"
        verbose_name = "Age Group"

    def __str__(self):
        return self.name


__all__ = ["AgeGroup", ]
