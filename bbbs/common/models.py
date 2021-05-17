from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

User = get_user_model()


class City(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Город'
    )
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Profile(models.Model):
    MODERATOR_GENERAL = 'Модератор "общий"'
    MODERATOR_REGIONAL = 'Модератор "региональный"'
    ADMIN = 'Администратор'
    MENTOR = 'Наставник'

    USER_TYPE_CHOICES = [
        (MODERATOR_GENERAL, 'moderator_general'),
        (MODERATOR_REGIONAL, 'moderator_regional'),
        (ADMIN, 'admin'),
        (MENTOR, 'mentor'),
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        verbose_name='Город',
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профайл"
        verbose_name_plural = "Профайлы"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, update_fields, created, **kwargs):
    try:
        instance.profile
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    if not created:
        if instance.role == Profile.MENTOR or not instance.role:
            instance.user.is_staff = False
        else:
            instance.user.is_staff = True
        if instance.role == Profile.ADMIN:
            instance.user.is_superuser = True
        else:
            instance.user.is_superuser = False
        if not instance.role:
            instance.user.is_active = False
        else:
            instance.user.is_active = True
        instance.user.save()


@receiver(post_delete, sender=Profile)
def update_user(sender, instance, *args, **kwargs):
    instance.user.delete()
