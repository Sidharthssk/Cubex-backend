from django.db import models
from category.models import Event, AgeGroup


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    contact = models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True)
    isEmailVerified = models.BooleanField(default=False)

    dob = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=10, default="")

    city = models.CharField(max_length=255, default="")
    state = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=255, default="")

    referredBy = models.CharField(max_length=55)
    isOnline = models.BooleanField(default=False)
    events = models.ManyToManyField(Event, blank=True)
    ageGroup = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = "participant"
        verbose_name_plural = "Participants"
        verbose_name = "Participant"

    def __str__(self):
        return self.name


__all__ = ["Participant"]
