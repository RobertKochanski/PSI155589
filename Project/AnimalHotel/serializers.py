from rest_framework import serializers
from .models import Species, User, Animal, Reservation


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['url', 'id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff',
                  'is_superuser', 'date_joined']
        # fields = '__all__'


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    species = serializers.SlugRelatedField(queryset=Species.objects.all(), slug_field='name')
    owner = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), view_name='user-detail')

    class Meta:
        model = Animal
        fields = ['url', 'id', 'name', 'age', 'species', 'owner']


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    animal = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='animal-detail')

    class Meta:
        model = Reservation
        fields = ['url', 'id', 'startDate', 'endDate', 'animal', 'comments', 'cost']
