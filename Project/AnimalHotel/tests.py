from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import Species, User
from rest_framework import status
from django.utils.http import urlencode
from django import urls
from django.contrib.auth.models import User


class SpeciesTests(APITestCase):

    def post_species(self, name):
        url = reverse(views.SpeciesList.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_species(self):
        new_species_name = 'gołąb'
        response = self.post_species(new_species_name)
        print("PK {0}".format(Species.objects.get().pk))
        assert response.status_code == status.HTTP_201_CREATED
        assert Species.objects.count() == 1
        assert Species.objects.get().name == new_species_name

    def test_post_existing_species_name(self):
        url = reverse(views.SpeciesList.name)
        new_species_name = 'Duplicate IT'
        data = {'name': new_species_name}
        response_one = self.post_species(new_species_name)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_species(new_species_name)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_species_by_name(self):
        species_name_one = 'dzik'
        species_name_two = 'lew'
        self.post_species(species_name_one)
        self.post_species(species_name_two)
        filter_by_name = {'name': species_name_one}
        url = '{0}?{1}'.format(reverse(views.SpeciesList.name), urlencode(filter_by_name))
        print(url)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == species_name_one


class UserTests(APITestCase):
    url = reverse(views.UserList.name)

    def post_user(self, username, password, client):
        url = reverse(views.UserList.name)
        data = {'username': username,
                'password': password,
                }
        response = client.post(url, data, format='json')
        return response

    def test_post_and_get_user(self):
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        user = APIClient()
        user.login(username='admin', password='admin123')
        new_username = 'user'
        new_password = 'user'
        response = self.post_user(new_username, new_password, user)
        assert response.status_code == status.HTTP_201_CREATED
        response = user.get(self.url)
        assert response.status_code == status.HTTP_200_OK




