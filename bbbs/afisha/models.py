from django.db import models

from bbbs.common.models import City, User


class Event(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
        verbose_name='Город',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес',
        help_text="Адрес места проведения мероприятия",
    )
    contact = models.CharField(
        max_length=200,
        verbose_name='Контакты',
    )
    start_at = models.DateTimeField(
        verbose_name='Дата начала',
    )
    end_at = models.DateTimeField(
        verbose_name='Дата окончания',
    )
    seats = models.PositiveIntegerField(
        verbose_name='Количество мест',
    )
    taken_seats = models.IntegerField(
        default=0,
        verbose_name='Количество занятых мест',
    )

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title


class EventParticipant(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    event = models.OneToOneField(
        Event,
        on_delete=models.RESTRICT
    )
