from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class City(models.Model):
    name = models.CharField("Город", max_length=30)
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)

    def __str__(self):
        return self.user.username
