from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from . import views
from .models import Species, User
from rest_framework import status
from django.utils.http import urlencode
from django import urls
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase

