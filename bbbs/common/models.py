from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Город'
    )
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MODERATOR_GENERAL = 'Модератор "общий"'
    MODERATOR_REGIONAL = 'Модератор "региональный"'
    ADMIN = 'Администратор'
    MENTOR = 'Наставник'

    USER_TYPE_CHOICES = [
        (MODERATOR_GENERAL, 'Модератор "общий"'),
        (MODERATOR_REGIONAL, 'Модератор "региональный"'),
        (ADMIN, 'Администратор'),
        (MENTOR, 'Наставник'),
    ]

    role = models.CharField(
        choices=USER_TYPE_CHOICES,
        blank=True,
        max_length=30,
        verbose_name='Роль',
        help_text="Выберите роль"
    )

    curator = models.EmailField(
        verbose_name='email куратора',
        max_length=255,
        blank=True,
    )
    city = models.ManyToManyField(
        City,
        blank=True,
        verbose_name='Город',
    )

    def save(self, *args, **kwargs):
        if self.role == User.ADMIN:
            self.is_superuser = True
            self.is_staff = True
        elif (self.role == User.MODERATOR_GENERAL or
              self.role == User.MODERATOR_REGIONAL):
            self.is_superuser = False
            self.is_staff = True
        elif self.role == User.MENTOR:
            self.is_superuser = False
            self.is_staff = False
        if self.is_superuser is True:
            self.role = User.ADMIN
        super(User, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Профайл"
        verbose_name_plural = "Профайлы"

    def __str__(self):
        return self.username
