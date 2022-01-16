from rest_framework import serializers
from .models import Species, User, Animal, Reservation


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AnimalSerializer(serializers.HyperlinkedRelatedField):
    species = serializers.SlugRelatedField(queryset=Species.objects.all(), slug_field='name')
    user = serializers.HyperlinkedRelatedField(many=False, queryset=User.objects.all(), view_name='user-detail')

    class Meta:
        model = Animal
        fields = '__all__'


class ReservationSerializer(serializers.HyperlinkedRelatedField):
    animal = serializers.HyperlinkedRelatedField(queryset=Animal.objects.all(), view_name='animal-detail')

    class Meta:
        model = Reservation
        fields = '__all__'
