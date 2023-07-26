from django.db import models
from accounts.models import Account


class Country(models.Model):
    code = models.IntegerField('Код страны', unique=True, null=True, blank=True)
    name = models.CharField('Название страны', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)
    currency = models.CharField('Валюта', max_length=50, blank=True, null=True)
    language = models.CharField('Язык', max_length=100, blank=True, null=True)
    timezone = models.CharField('Часовой пояс', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class City(models.Model):
    code = models.IntegerField('Код города', unique=True, null=True, blank=True)
    name = models.CharField('Название города', max_length=255)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, related_name='cities', verbose_name='Страна')
    description = models.TextField('Описание', blank=True, null=True)
    is_capital = models.BooleanField('Столица', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class TrainType(models.Model):
    name = models.CharField('Тип поезда', max_length=100)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип поезда'
        verbose_name_plural = 'Типы поездов'


class Train(models.Model):
    name = models.CharField('Название поезда', max_length=255)
    number = models.CharField('Номер поезда', max_length=50, unique=True)
    train_type = models.ForeignKey(TrainType, on_delete=models.PROTECT, verbose_name='Тип поезда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'


class TrainStation(models.Model):
    # class StationType(models.TextChoices):
    #     TYPE_1 = 'type_1', "Тип станции 1"
    #     TYPE_2 = 'type_2', "Тип станции 2"
    #     TYPE_3 = 'type_3', "Тип станции 3"

    name = models.CharField(max_length=100, unique=True, verbose_name="Название станции")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="train_stations", verbose_name="Страна")
    # station_type = models.CharField(max_length=10, choices=StationType.choices, default=StationType.TYPE_1,
    #                                 verbose_name="Тип станции", blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name="Адрес")
    latitude = models.DecimalField(max_digits=19, decimal_places=15, blank=True, null=True, verbose_name="Широта")
    longitude = models.DecimalField(max_digits=19, decimal_places=15, blank=True, null=True, verbose_name="Долгота")

    class Meta:
        verbose_name = "Железнодорожная станция"
        verbose_name_plural = "Железнодорожные станции"

    def __str__(self):
        return self.name


class TrainSchedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE, verbose_name='Поезд')
    train_type = models.ForeignKey(TrainType, on_delete=models.PROTECT, related_name='schedules',
                                   verbose_name='Тип поезда')
    departure_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departure_schedules',
                                       verbose_name='Город отправления')
    arrival_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrival_schedules',
                                     verbose_name='Город прибытия')
    departure_datetime = models.DateTimeField('Дата и время отправления', null=True, blank=True, default=None)
    arrival_datetime = models.DateTimeField('Дата и время прибытия', null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.train} ({self.train_type}) - {self.departure_city} to {self.arrival_city}"

    class Meta:
        verbose_name = 'Расписание поезда'
        verbose_name_plural = 'Расписания поездов'


class Seat(models.Model):
    schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE, related_name='seats',
                                 verbose_name='Расписание поезда')
    seat_number = models.CharField('Номер места', max_length=10)
    is_booked = models.BooleanField('Забронировано', default=False)
    passenger = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пассажир')
    booked_at = models.DateTimeField('Дата и время бронирования', null=True, blank=True)

    def __str__(self):
        return f"{self.schedule} - Место {self.seat_number}"

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Ticket(models.Model):
    schedule = models.ForeignKey(TrainSchedule, on_delete=models.CASCADE, verbose_name='Расписание поезда')
    passenger = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='tickets', verbose_name='Пассажир')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Место')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.schedule} - {self.passenger} - {self.seat}"

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
