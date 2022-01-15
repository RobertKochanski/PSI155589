from rest_framework import serializers
from .models import Species, User, Animal, Reservation


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'url', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'firstname', 'lastname', 'email', 'password']


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    species = serializers.SlugRelatedField(queryset=Species.objects.all(), slug_field='name')
    user = serializers.HyperlinkedRelatedField(many=False, queryset=User.objects.all(), view_name='user-detail')

    class Meta:
        model = Animal
        fields = ['id', 'url', 'name', 'age', 'species', 'user']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    animal = serializers.HyperlinkedRelatedField(queryset=Animal.objects.all(), view_name='animal-detail')

    class Meta:
        model = Reservation
        fields = ['id', 'url', 'startDate', 'endDate', 'user', 'animal', 'comments', 'cost']
