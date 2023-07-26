# Generated by Django 4.2.3 on 2023-07-25 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_city_description_city_is_capital_country_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainschedule',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='trainschedule',
            name='departure_time',
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='arrival_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Arrival Date and Time'),
        ),
        migrations.AddField(
            model_name='trainschedule',
            name='departure_datetime',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Departure Date and Time'),
        ),
    ]