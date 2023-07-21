from django.db import models

from accounts.models import Account


class Country(models.Model):
    code = models.IntegerField('Country Code', unique=True, null=True, blank=True)
    name = models.CharField('Country Name', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class City(models.Model):
    code = models.IntegerField('City Code', unique=True, null=True, blank=True)
    name = models.CharField('City Name', max_length=255)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='cities', verbose_name='Country')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class TrainType(models.Model):
    name = models.CharField('Train Type', max_length=100)
    description = models.TextField('Description', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Train Type'
        verbose_name_plural = 'Train Types'


class Train(models.Model):
    name = models.CharField('Train Name', max_length=255)
    number = models.CharField('Train Number', max_length=50, unique=True)
    train_type = models.ForeignKey(TrainType, on_delete=models.PROTECT, verbose_name='Train Type')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Train'
        verbose_name_plural = 'Trains'


class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, verbose_name='Train')
    train_type = models.ForeignKey(TrainType, on_delete=models.PROTECT, related_name='schedules',
                                   verbose_name='Train Type')
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_schedules',
                                       verbose_name='Departure City')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_schedules',
                                     verbose_name='Arrival City')
    departure_time = models.TimeField('Departure Time')
    arrival_time = models.TimeField('Arrival Time')

    def __str__(self):
        return f"{self.train} ({self.train_type}) - {self.departure_city} to {self.arrival_city}"

    class Meta:
        verbose_name = 'Train Schedule'
        verbose_name_plural = 'Train Schedules'


class Seat(models.Model):
    schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE, related_name='seats',
                                 verbose_name='Train Schedule')
    seat_number = models.CharField('Seat Number', max_length=10)
    is_booked = models.BooleanField('Is Booked', default=False)
    passenger = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Passenger')
    booked_at = models.DateTimeField('Booked Date and Time', null=True, blank=True)

    def __str__(self):
        return f"{self.schedule} - Seat {self.seat_number}"

    class Meta:
        verbose_name = 'Seat'
        verbose_name_plural = 'Seats'


class Ticket(models.Model):
    schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE, verbose_name='Train Schedule')
    passenger = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tickets', verbose_name='Passenger')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Seat')
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.schedule} - {self.passenger} - {self.seat}"

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
