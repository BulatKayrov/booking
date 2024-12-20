from django.db import models


class IsFreeChoice(models.TextChoices):
    FREE = 'FREE', 'Свободен'
    BUSY = 'BUSY', 'Занят'


class StatusBooking(models.TextChoices):
    CONFIRMED = 'CONFIRMED', 'Подтверждено'
    CANCELLED = 'CANCELLED', 'Отменено'
    PROCESSING = 'PROCESSING', 'Обрабатывается'