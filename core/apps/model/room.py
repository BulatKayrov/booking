from django.db import models

from core.apps.model.choices import IsFreeChoice


class Room(models.Model):
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    type_room = models.PositiveSmallIntegerField(verbose_name='Тип комнаты', default=1)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    is_free = models.CharField(verbose_name='Статус', default=IsFreeChoice.FREE, choices=IsFreeChoice.choices, max_length=50)
    hotel = models.ForeignKey(verbose_name='Отель', to='Hotel', on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return f'Room {self.pk}'
