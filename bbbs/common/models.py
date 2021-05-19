from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.enums import Choices
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class City(models.Model):
    name = models.CharField(max_length=30)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Profile(models.Model):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        MODERATOR = 'moderator', 'Модератор'
        REGION_MODERATOR = 'region_moderator', 'Региональный модератор'
        MENTOR = 'mentor', 'Наставник'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profiles')
    city = models.OneToOneField(
        City, on_delete=models.RESTRICT, null=True, blank=True)
    role = models.CharField(
        max_length=100, choices=Roles.choices, default=Roles.MENTOR)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
