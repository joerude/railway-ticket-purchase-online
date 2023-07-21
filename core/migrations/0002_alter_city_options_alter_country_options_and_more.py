# Generated by Django 4.2.3 on 2023-07-21 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='seat',
            options={'verbose_name': 'Seat', 'verbose_name_plural': 'Seats'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Ticket', 'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterModelOptions(
            name='train',
            options={'verbose_name': 'Train', 'verbose_name_plural': 'Trains'},
        ),
        migrations.AlterModelOptions(
            name='trainschedule',
            options={'verbose_name': 'Train Schedule', 'verbose_name_plural': 'Train Schedules'},
        ),
        migrations.AlterModelOptions(
            name='traintype',
            options={'verbose_name': 'Train Type', 'verbose_name_plural': 'Train Types'},
        ),
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='City Code'),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='core.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, verbose_name='City Name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Country Code'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Country Name'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='booked_at',
            field=models.DateField(blank=True, null=True, verbose_name='Booked Date'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='is_booked',
            field=models.BooleanField(default=False, verbose_name='Is Booked'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='passenger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Passenger'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='core.trainschedule', verbose_name='Train Schedule'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(max_length=10, verbose_name='Seat Number'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='passenger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='Passenger'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trainschedule', verbose_name='Train Schedule'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.seat', verbose_name='Seat'),
        ),
        migrations.AlterField(
            model_name='train',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Train Name'),
        ),
        migrations.AlterField(
            model_name='train',
            name='number',
            field=models.CharField(max_length=50, unique=True, verbose_name='Train Number'),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.traintype', verbose_name='Train Type'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='arrival_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_schedules', to='core.city', verbose_name='Arrival City'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='arrival_time',
            field=models.TimeField(verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='departure_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_schedules', to='core.city', verbose_name='Departure City'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='departure_time',
            field=models.TimeField(verbose_name='Departure Time'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.train', verbose_name='Train'),
        ),
        migrations.AlterField(
            model_name='trainschedule',
            name='train_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedules', to='core.traintype', verbose_name='Train Type'),
        ),
        migrations.AlterField(
            model_name='traintype',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='traintype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Train Type'),
        ),
    ]