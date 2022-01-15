from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics
from .models import Species, User, Animal, Reservation
from .serializers import SpeciesSerializer, UserSerializer, AnimalSerializer, ReservationSerializer


class SpeciesList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    name = 'species-list'
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    name = 'species-detail'
    permission_classes = [permissions.IsAdminUser]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ['name', 'surname', 'email']
    search_fields = ['surname', 'email']
    ordering_fields = ['name', 'surname', 'email']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated]


class AnimalList(generics.ListCreateAPIView):
    serializer_class = AnimalSerializer
    name = 'animal-list'
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ['name', 'age']
    search_fields = ['name']
    ordering_fields = ['name', 'age']


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = 'animal-detail'
    permission_classes = [permissions.IsAuthenticated]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAdminUser]
    name = 'reservation-list'


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    name = 'reservation-detail'
