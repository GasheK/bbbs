from django.contrib.auth import get_user_model
from django.db import models
from user.models import City

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='profile')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='город', related_name='profile')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'profiles'
        constraints = [
            models.UniqueConstraint(fields=['user', 'city'],
                                    name='unique profile')
        ]
