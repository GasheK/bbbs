from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class City(models.Model):
    name = models.CharField(verbose_name='Название города', max_length=30)
    is_primary = models.BooleanField(
        verbose_name='Основной',
        default=False)

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
        User, on_delete=models.CASCADE, related_name='profiles',
        verbose_name='Пользователь')
    city = models.ManyToManyField(
        City, null=True, blank=True, verbose_name='Город')
    role = models.CharField(
        max_length=100, choices=Roles.choices, default=Roles.MENTOR,
        verbose_name='Роль')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def full_name(self):
        name = self.user.get_full_name()
        if name:
            return self.user.get_full_name()
        return self.user.username

    def email(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """ При создании нового пользователя, создаем Profile."""
    if created:
        if instance.is_superuser:
            Profile.objects.create(user=instance, role=sender.Roles.ADMIN)
        else:
            Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def save_profile_user(sender, instance, **kwargs):
    """
    При изменении роли в модели Profile меняем у юзера значения
    полей is_superuser и is_staff и меняем Permissions.
    """
    roles = sender.Roles
    if instance.role == roles.ADMIN:
        instance.user.is_superuser = True
        instance.user.is_staff = True
    elif instance.role in (roles.MODERATOR, roles.REGION_MODERATOR):
        instance.user.is_superuser = False
        instance.user.is_staff = True
        permissions = Permission.objects.filter(
            models.Q(codename__endswith='event')
            | models.Q(codename__endswith='eventparticipant'))
        if instance.role == roles.MODERATOR:
            permissions = permissions | Permission.objects.filter(
                models.Q(codename='view_city')
                | models.Q(codename='view_profile'))
        instance.user.user_permissions.clear()
        instance.user.user_permissions.add(*permissions)
    else:
        instance.user.is_superuser = False
        instance.user.is_staff = False
        instance.user.user_permissions.clear()
    instance.user.save()
