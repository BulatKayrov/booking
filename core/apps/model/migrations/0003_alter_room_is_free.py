# Generated by Django 3.2.9 on 2024-12-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_auto_20241220_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='is_free',
            field=models.BooleanField(choices=[('1', 'Свободен'), ('0', 'занят')], default=True, verbose_name='Статус'),
        ),
    ]