from django.contrib.auth import get_user_model
from django.db import models

from cities.models import City


User = get_user_model()


class Event(models.Model):
    address = models.CharField(max_length=200, verbose_name='адрес')
    contact = models.CharField(max_length=200, verbose_name='контакт')
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    start_at = models.DateTimeField(verbose_name='начало')
    end_at = models.DateTimeField(verbose_name='окончание')
    seats = models.IntegerField(verbose_name='количество мест')
    taken_seats = models.IntegerField(default=0, verbose_name='количество занятых мест')
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, verbose_name='город', related_name='events')

    def __str__(self):
        return self.title


class EventParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='participates')
    event = models.ForeignKey(Event, on_delete=models.PROTECT, verbose_name='мероприятие', related_name='participants')

    class Meta:
        verbose_name_plural = 'participate'
        constraints = [
            models.UniqueConstraint(fields=['user', 'event'],
                                    name='unique participate')
        ]
