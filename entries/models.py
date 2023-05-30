from django.db import models
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Текст записи')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Записи'