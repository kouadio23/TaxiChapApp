# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Vehicle, Reservation

# Configuration de l'administration pour le modèle User personnalisé
class CustomUserAdmin(UserAdmin):
    # Ajoutez ou modifiez les champs que vous souhaitez afficher dans l'interface d'administration.
    # UserAdmin contient déjà beaucoup de configurations utiles, mais vous pouvez les étendre
    # ou les modifier selon vos besoins.
    model = User
    list_display = ['username', 'email', 'phone_number', 'is_staff']

# Administration pour le modèle Vehicle
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'plate_number', 'vehicle_type', 'owner']
    list_filter = ['vehicle_type', 'make']
    search_fields = ['plate_number', 'make', 'model']

# Administration pour le modèle Reservation
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['passenger', 'vehicle', 'start_location', 'end_location', 'start_time', 'status']
    list_filter = ['status', 'start_time']
    search_fields = ['passenger__username', 'vehicle__plate_number']

# Enregistrement des modèles dans l'interface d'administration
admin.site.register(User, CustomUserAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Reservation, ReservationAdmin)
