from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsAdmin, IsDispatcher

from .models import Country, City, TrainType, Train, TrainSchedule, Seat, Ticket
from .serializers import (
    CountrySerializer, CitySerializer, TrainTypeSerializer,
    TrainSerializer, TrainScheduleSerializer, SeatSerializer, TicketSerializer, CountryDetailSerializer
)


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAdmin,)


# class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer
#     permission_classes = (IsAdmin,)


class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAdmin,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CountryDetailSerializer
        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        response_data = {
            "data": data,
            "status": "Success",
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        response_data = {
            "data": serializer.data,
            "status": "Success",
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        response_data = {
            "status": "Success",
            "message": "Country deleted successfully.",
        }

        return Response(response_data, status=status.HTTP_204_NO_CONTENT)


class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAdmin,)


class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAdmin,)


class TrainTypeListCreateView(generics.ListCreateAPIView):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TrainTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TrainListCreateView(generics.ListCreateAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TrainRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TrainScheduleListCreateView(generics.ListCreateAPIView):
    queryset = TrainSchedule.objects.all()
    serializer_class = TrainScheduleSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TrainScheduleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainSchedule.objects.all()
    serializer_class = TrainScheduleSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class SeatRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TicketListCreate(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TicketRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsAdmin, IsDispatcher,)


class TripHistoryView(generics.RetrieveAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        trip_id = self.kwargs['trip_id']
        try:
            schedule = TrainSchedule.objects.get(id=trip_id)
            return Seat.objects.filter(schedule=schedule)
        except TrainSchedule.DoesNotExist:
            return Seat.objects.none()

    def retrieve(self, request, *args, **kwargs):
        seats = self.get_queryset()
        booked_seats = seats.filter(is_booked=True).count()
        available_seats = seats.filter(is_booked=False).count()

        serializer = self.get_serializer(seats, many=True)
        response_data = {
            "trip_id": kwargs['trip_id'],
            "train_name": seats[0].schedule.train.name,
            "departure_city": seats[0].schedule.departure_city.name,
            "arrival_city": seats[0].schedule.arrival_city.name,
            "departure_time": seats[0].schedule.departure_time.isoformat(),
            "arrival_time": seats[0].schedule.arrival_time.isoformat(),
            "total_seats": seats.count(),
            "available_seats": available_seats,
            "booked_seats": booked_seats,
            "seats": serializer.data
        }

        return Response(response_data)
