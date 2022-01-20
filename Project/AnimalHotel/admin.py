from django.contrib import admin
from .models import Species, Reservation, Animal


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass
