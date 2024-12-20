# Generated by Django 3.2.9 on 2024-12-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_alter_room_is_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='is_free',
            field=models.CharField(choices=[('FREE', 'Свободен'), ('BUSY', 'Занят')], default='FREE', max_length=50, verbose_name='Статус'),
        ),
    ]