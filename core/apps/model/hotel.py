from django.db import models


class Hotel(models.Model):
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    title = models.CharField(verbose_name='Название отеля', max_length=255)
    address = models.TextField(verbose_name='Адресс', max_length=500)
    description = models.TextField(verbose_name='Описание', max_length=500)


    def rating(self):
        pass

    def __str__(self):
        return self.title
