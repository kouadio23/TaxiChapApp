from django.apps import AppConfig


class ReservationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservations'



# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ReservationViewSet, VehicleViewSet

# # Création d'un router et enregistrement de nos viewsets
# router = DefaultRouter()
# router.register(r'reservations', ReservationViewSet)
# router.register(r'vehicles', VehicleViewSet)

# # Les URLs de l'API sont maintenant déterminées automatiquement par le router
# urlpatterns = [
#     path('', include(router.urls)),
# ]
