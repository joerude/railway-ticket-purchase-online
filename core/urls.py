# core/urls.py
from django.urls import path
from .views import (
    CountryListCreateView, CountryRetrieveUpdateDestroyView,
    CityListCreateView, CityRetrieveUpdateDestroyView,
    TrainTypeListCreateView, TrainTypeRetrieveUpdateDestroyView,
    TrainListCreateView, TrainRetrieveUpdateDestroyView,
    TrainScheduleListCreateView, TrainScheduleRetrieveUpdateDestroyView,
    SeatListCreateView, SeatRetrieveUpdateDestroyAPIView,
    TicketListCreate, TicketRetrieveUpdateDestroy, TripHistoryView,
)

urlpatterns = [
    path('countries/', CountryListCreateView.as_view(), name='country-list'),
    path('countries/<int:pk>/', CountryRetrieveUpdateDestroyView.as_view(), name='country-detail'),
    path('cities/', CityListCreateView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
    path('traintypes/', TrainTypeListCreateView.as_view(), name='traintype-list'),
    path('traintypes/<int:pk>/', TrainTypeRetrieveUpdateDestroyView.as_view(), name='traintype-detail'),
    path('trains/', TrainListCreateView.as_view(), name='train-list'),
    path('trains/<int:pk>/', TrainRetrieveUpdateDestroyView.as_view(), name='train-detail'),
    path('trainschedules/', TrainScheduleListCreateView.as_view(), name='trainschedule-list'),
    path('trainschedules/<int:pk>/', TrainScheduleRetrieveUpdateDestroyView.as_view(), name='trainschedule-detail'),
    path('seats/', SeatListCreateView.as_view(), name='seat-list'),
    path('seats/<int:pk>/', SeatRetrieveUpdateDestroyAPIView.as_view(), name='seat-detail'),
    path('tickets/', TicketListCreate.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketRetrieveUpdateDestroy.as_view(), name='ticket-detail'),

    path('trip-history/<int:trip_id>/', TripHistoryView.as_view(), name='trip-history'),
]
