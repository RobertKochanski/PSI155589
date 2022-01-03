from rest_framework import serializers
from .models import Species, Owner, Animal, Reservation


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'url', 'name']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'url', 'firstname', 'lastname', 'email', 'password']


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    species = serializers.SlugRelatedField(queryset=Species.objects.all(), slug_field='name')
    owner = serializers.HyperlinkedRelatedField(many=False, queryset=Owner.objects.all(), view_name='user-detail')

    class Meta:
        model = Animal
        fields = ['id', 'url', 'name', 'age', 'species', 'owner']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    animal = serializers.HyperlinkedRelatedField(queryset=Animal.objects.all(), view_name='animal-detail')

    class Meta:
        model = Reservation
        fields = ['id', 'url', 'startDate', 'endDate', 'user', 'animal', 'comments', 'cost']
