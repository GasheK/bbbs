from django.db import models

from bbbs.common.models import Tag


class Question(models.Model):
    tag = models.ManyToManyField(Tag, related_name='tags')
    question = models.CharField(max_length=500, unique=True)
    answer = models.TextField(verbose_name='Ответ на вопрос')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def list_tags(self):
        return self.tag.values_list('name')

    def __str__(self):
        return self.question
