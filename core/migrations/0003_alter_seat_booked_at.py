# Generated by Django 4.2.3 on 2023-07-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_city_options_alter_country_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='booked_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Booked Date and Time'),
        ),
    ]
