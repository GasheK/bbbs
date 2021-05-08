from django.db import models

from bbbs.common.models import City


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
