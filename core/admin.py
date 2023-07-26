from django.contrib import admin
from .models import Country, City, TrainType, Train, TrainSchedule, Seat, Ticket, TrainStation


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'currency', 'language', 'timezone')
    search_fields = ('name', 'code')
    list_filter = ('currency', 'language', 'timezone')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'is_capital')
    search_fields = ('name', 'country__name')
    list_filter = ('country', 'is_capital')


@admin.register(TrainType)
class TrainTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'train_type')
    search_fields = ('name', 'number')
    list_filter = ('train_type',)


@admin.register(TrainSchedule)
class TrainScheduleAdmin(admin.ModelAdmin):
    list_display = ('train', 'train_type', 'departure_city', 'arrival_city', 'departure_datetime', 'arrival_datetime')
    search_fields = ('train__name', 'train__number', 'departure_city__name', 'arrival_city__name')
    list_filter = ('train_type', 'departure_city', 'arrival_city')


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'seat_number', 'is_booked', 'passenger', 'booked_at')
    search_fields = ('schedule__train__name', 'schedule__departure_city__name', 'schedule__arrival_city__name')
    list_filter = ('is_booked',)


@admin.register(TrainStation)
class TrainStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_country_name', 'address', 'latitude', 'longitude')
    search_fields = ('name', 'country__name', 'address')

    def get_country_name(self, obj):
        return obj.country.name if obj.country else None

    get_country_name.short_description = 'Country'


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('schedule', 'passenger', 'seat', 'price')
    search_fields = ('schedule__train__name', 'schedule__departure_city__name', 'schedule__arrival_city__name',
                     'passenger__username')
    list_filter = ('price',)
