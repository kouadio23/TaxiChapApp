from django.urls import path
from .views import ReservationList, ReservationCreate

urlpatterns = [
    path('reservations/', ReservationList.as_view(), name='reservation_list'),
    path('reservations/create/', ReservationCreate.as_view(), name='reservation_create'),
]
