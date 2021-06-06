from django.db import models
from django.utils.translation import gettext_lazy

from bbbs.common.models import Tag, City


class Place(models.Model):
    class Genders(models.TextChoices):
        MALE = "M", gettext_lazy("Мальчик")
        FEMALE = "F", gettext_lazy("Девочка")

    class ActivityTypes(models.IntegerChoices):
        ACTIVE = 0, gettext_lazy("Активный")
        ENTERTAINING = 1, gettext_lazy("Развлекательный")
        INFORMATIVE = 2, gettext_lazy("Познавательный")

    chosen = models.BooleanField(
        verbose_name="Выбор наставника",
        default=False,
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    address = models.CharField(
        verbose_name="Адрес",
        max_length=200,
    )
    gender = models.CharField(
        verbose_name="Пол",
        choices=Genders.choices,
        max_length=1,
        null=True,
        blank=True,
    )
    age = models.PositiveSmallIntegerField(
        verbose_name="Возраст",
    )
    activity_type = models.PositiveSmallIntegerField(
        verbose_name="Тип отдыха",
        choices=ActivityTypes.choices,
    )
    description = models.TextField(
        verbose_name="Комментарий",
        help_text="Поделитесь впечатлениями о проведенном времени",
    )
    link = models.URLField(
        verbose_name="Сайт",
        help_text="Введите адрес сайта",
        null=True,
        blank=True,
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name="Тег",
    )
    imageUrl = models.ImageField(
        verbose_name="Фото",
        help_text="Добавить фото",
        null=True,
        blank=True,
        upload_to="places/",
    )
    class Meta:
        verbose_name = "Место - куда пойти?"
        verbose_name_plural = "Места - куда пойти?"

    def __str__(self):
        return self.title

    def get_gender(self, gender_code):
        return self.Genders(gender_code).label

    def get_activity_type(self, type_code):
        return self.ActivityTypes(type_code).label
