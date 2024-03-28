from django.shortcuts import render
from django.views import View
from .models import Reservation, Vehicle
from django.http import JsonResponse

from rest_framework import viewsets, serializers

from .serializers import ReservationSerializer, VehicleSerializer
# Vue pour lister toutes les réservations
class ReservationList(View):
    def get(self, request, *args, **kwargs):
        reservations = Reservation.objects.all()
        data = {"reservations": list(reservations.values("passenger", "vehicle", "start_location", "end_location", "status"))}
        return JsonResponse(data)

# Vue pour créer une nouvelle réservation
class ReservationCreate(View):
    def post(self, request, *args, **kwargs):
        # Ici, vous traiteriez les données POST pour créer une nouvelle réservation.
        # Cette partie est simplifiée pour l'exemple.
        return JsonResponse({"message": "Nouvelle réservation créée"}, status=201)


# Create your views here.




# # Créez un serializer pour le modèle Reservation
# class ReservationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reservation
#         fields = ['passenger', 'vehicle', 'start_location', 'end_location', 'status']

# # Créez un viewset pour le modèle Reservation
# class ReservationViewSet(viewsets.ModelViewSet):
#     queryset = Reservation.objects.all()
#     serializer_class = ReservationSerializer