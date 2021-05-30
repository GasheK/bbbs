from django.contrib.auth.models import AbstractUser
from django.db.models import (Model, CharField, EmailField,
                              TextChoices, BooleanField, ManyToManyField)
#from cities.models import City


class City(Model):
    name = CharField(max_length=30)
    is_primary = BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class User(AbstractUser):
    """User augmented fields."""

    class RoleUser(TextChoices):
        USER = 'user', 'Пользователь'
        MENTOR = 'mentor', 'Наставник'
        MODERATOR = 'moderator', 'Модератор'
        MODERATOR_REG = 'moderator_reg', 'Модератор региональный'
        ADMIN = 'admin', 'Администратор'

    role = CharField(
        verbose_name='role',
        max_length=50,
        blank=True,
        choices=RoleUser.choices,
        default=RoleUser.USER
    )
    email = EmailField(
        verbose_name='email',
        max_length=255,
        unique=True
    )
    city = ManyToManyField(
        City,
        related_name='users',
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_staff or self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_moderator_reg(self):
        return self.role == 'moderator_reg'

    @property
    def is_mentor(self):
        return self.role == 'mentor'
