from django.db import models


class Start(models.Model):
    value = models.PositiveSmallIntegerField(default=0, verbose_name='Значение')
    hotel = models.ForeignKey(to='Hotel', on_delete=models.CASCADE, related_name='stars')

    class Meta:
        verbose_name = 'Звезда'
        verbose_name_plural = 'Звезды'

    def __str__(self):
        return f'Star {self.value}'