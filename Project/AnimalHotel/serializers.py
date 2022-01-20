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


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    species = serializers.SlugRelatedField(queryset=Species.objects.all(), slug_field='name')
    # nie działa
    # owner = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Animal
        fields = ['id', 'name', 'age', 'species', 'owner']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    # nie działa
    # animal = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='animal-detail')
    animal = serializers.ReadOnlyField(source='animal.name')

    class Meta:
        model = Reservation
        fields = ['id', 'startDate', 'endDate', 'animal', 'comments', 'cost']
