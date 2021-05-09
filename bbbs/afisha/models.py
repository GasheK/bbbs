from django.contrib.auth import get_user_model
from django.db import models

from bbbs.common.models import City


User = get_user_model()


class Event(models.Model):
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    seats = models.IntegerField()
    taken_seats = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title


class EventParticipant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.OneToOneField(Event, on_delete=models.RESTRICT)
