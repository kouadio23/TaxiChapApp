
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle Utilisateur Personnalisé
class User(AbstractUser):
    # Ajoutez des champs supplémentaires spécifiques à votre application si nécessaire
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    # Vous pouvez ajouter plus de champs personnalisés ici
    # Redéfinition des champs pour corriger les conflits d'accesseur inverses
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="user_set_custom",  # Utilisez un nom unique pour related_name
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="user_set_custom_permissions",  # Utilisez un nom unique pour related_name
        related_query_name="user",
    )

# Modèle pour les Véhicules
class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
        ('tricycle', 'Tricycle'),
    ]
    make = models.CharField(max_length=50)  # Marque du véhicule
    model = models.CharField(max_length=50)  # Modèle du véhicule
    plate_number = models.CharField(max_length=20, unique=True)  # Numéro d'immatriculation
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)  # Type de véhicule
    owner = models.ForeignKey(User, related_name='vehicles', on_delete=models.CASCADE)  # Propriétaire du véhicule

    def __str__(self):
        return f"{self.make} {self.model} - {self.plate_number}"

# Modèle pour les Réservations
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    passenger = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, related_name='reservations', on_delete=models.SET_NULL, null=True)
    start_location = models.CharField(max_length=255)  # Emplacement de départ
    end_location = models.CharField(max_length=255)  # Destination
    start_time = models.DateTimeField()  # Heure de début
    end_time = models.DateTimeField(null=True, blank=True)  # Heure de fin (peut ne pas être définie immédiatement)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Statut de la réservation

    def __str__(self):
        return f"Reservation from {self.start_location} to {self.end_location} by {self.passenger}"
