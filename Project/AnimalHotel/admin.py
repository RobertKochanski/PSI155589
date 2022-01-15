from django.contrib import admin
from .models import User, Species, Reservation, Animal

admin.site.register(User)


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass
