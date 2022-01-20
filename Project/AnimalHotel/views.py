from django_filters import FilterSet, DateTimeFilter
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Species, User, Animal, Reservation
from .serializers import SpeciesSerializer, UserSerializer, AnimalSerializer, ReservationSerializer
from .custompermission import IsOwnerOrAdmin


class SpeciesList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    name = 'species-list'
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']


class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    name = 'species-detail'
    permission_classes = [permissions.AllowAny]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ['username', 'email']
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'email']


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [IsOwnerOrAdmin]


class AnimalList(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = 'animal-list'
    permission_classes = [permissions.IsAdminUser]
    filterset_fields = ['name', 'age']
    search_fields = ['name']
    ordering_fields = ['name', 'age', 'species']


class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    name = 'animal-detail'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]


class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAdminUser]
    name = 'reservation-list'
    ordering_fields = ['startDate', 'endDate', 'cost']


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]
    name = 'reservation-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'species': reverse(SpeciesList.name, request=request),
            'user': reverse(UserList.name, request=request),
            'animals': reverse(AnimalList.name, request=request),
            'reservations': reverse(ReservationList.name, request=request)
        })

