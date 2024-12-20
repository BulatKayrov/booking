from core.apps.model.choices import StatusBooking
from django.db import models


class Booking(models.Model):
    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Бронирование'

    user = models.ForeignKey(to='User', on_delete=models.CASCADE, related_name='bookings', verbose_name='Пользователь')
    room = models.ManyToManyField(to='Room', related_name='bookings', verbose_name='Номер')
    check_in = models.DateTimeField(verbose_name='Дата заезда')
    check_out = models.DateTimeField(verbose_name='Дата выезда')
    status = models.CharField(
        default=StatusBooking.PROCESSING,
        choices=StatusBooking.choices,
        verbose_name='Статус',
        max_length=50
    )

    def __str__(self):
        return f'booking {self.pk}'
