# Generated by Django 3.2.9 on 2024-12-20 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название отеля')),
                ('address', models.TextField(max_length=500, verbose_name='Адресс')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starts', to='model.hotel')),
            ],
            options={
                'verbose_name': 'Звезда',
                'verbose_name_plural': 'Звезды',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_room', models.PositiveSmallIntegerField(default=1, verbose_name='Тип комнаты')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('is_free', models.BooleanField(choices=[('FREE', 'Свободен'), ('BUSY', 'занят')], default='FREE', verbose_name='Статус')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='model.hotel', verbose_name='Отель')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(verbose_name='Дата заезда')),
                ('check_out', models.DateTimeField(verbose_name='Дата выезда')),
                ('status', models.BooleanField(choices=[('CONFIRMED', 'Подтверждено'), ('CANCELLED', 'Отменено'), ('PROCESSING', 'Обрабатывается')], default='PROCESSING', verbose_name='Статус')),
                ('room', models.ManyToManyField(related_name='bookings', to='model.Room', verbose_name='Номер')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Бронирование',
            },
        ),
    ]
