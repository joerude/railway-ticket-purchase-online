# core/serializers.py
from rest_framework import serializers

from accounts.models import Account
from .models import Country, City, TrainType, Train, TrainSchedule, Seat, Ticket


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'code', 'name', 'population',
                  'capital', 'language', 'currency')


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = '__all__'


class TrainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainType
        fields = '__all__'


class TrainSerializer(serializers.ModelSerializer):
    train_type = TrainTypeSerializer()

    class Meta:
        model = Train
        fields = '__all__'


class TrainScheduleSerializer(serializers.ModelSerializer):
    train = TrainSerializer()
    departure_city = CitySerializer()
    arrival_city = CitySerializer()

    class Meta:
        model = TrainSchedule
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('schedule', 'seat_number', 'is_booked', 'passenger', 'booked_at')


class TicketSerializer(serializers.ModelSerializer):
    schedule = TrainScheduleSerializer()
    passenger = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    seat = SeatSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'
