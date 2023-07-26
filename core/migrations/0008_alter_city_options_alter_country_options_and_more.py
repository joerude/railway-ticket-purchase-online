# Generated by Django 4.2.3 on 2023-07-25 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_alter_trainstation_country_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='seat',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Билет', 'verbose_name_plural': 'Билеты'},
        ),
        migrations.AlterModelOptions(
            name='train',
            options={'verbose_name': 'Поезд', 'verbose_name_plural': 'Поезда'},
        ),
        migrations.AlterModelOptions(
            name='trainschedule',
            options={'verbose_name': 'Расписание поезда', 'verbose_name_plural': 'Расписания поездов'},
        ),
        migrations.AlterModelOptions(
            name='traintype',
            options={'verbose_name': 'Тип поезда', 'verbose_name_plural': 'Типы поездов'},
        ),
        migrations.RemoveField(
            model_name='trainstation',
            name='station_type',
        ),
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Код города'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='core.country', verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='city',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='city',
            name='is_capital',
            field=models.BooleanField(default=False, verbose_name='Столица'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название города'),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Код страны'),
        ),
        migrations.AlterField(
            model_name='country',
            name='currency',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='country',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Язык'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название страны'),
        ),
        migrations.AlterField(
            model_name='country',
            name='timezone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Часовой пояс'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='booked_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата и время бронирования'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='is_booked',
            field=models.BooleanField(default=False, verbose_name='Забронировано'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='passenger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пассажир'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='core.trainschedule', verbose_name='Расписание поезда'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(max_length=10, verbose_name='Номер места'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='Пассажир'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trainschedule', verbose_name='Расписание поезда'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.seat', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='train',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название поезда'),
        ),
        migrations.AlterField(
            model_name='train',
            name='number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Номер поезда'),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.traintype', verbose_name='Тип поезда'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='arrival_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_schedules', to='core.city', verbose_name='Город прибытия'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='arrival_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата и время прибытия'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='departure_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_schedules', to='core.city', verbose_name='Город отправления'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='departure_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата и время отправления'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.train', verbose_name='Поезд'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='train_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedules', to='core.traintype', verbose_name='Тип поезда'),
        ),
        migrations.AlterField(
            model_name='traintype',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='traintype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Тип поезда'),
        ),
    ]