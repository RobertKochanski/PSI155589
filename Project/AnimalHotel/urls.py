from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),

    path('species', views.SpeciesList.as_view(), name=views.SpeciesList.name),
    path('species/<int:pk>', views.SpeciesDetail.as_view(), name=views.SpeciesDetail.name),

    path('user', views.UserList.as_view(), name=views.UserList.name),
    path('user/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),

    path('animal', views.AnimalList.as_view(), name=views.AnimalList.name),
    path('animal/<int:pk>', views.AnimalDetail.as_view(), name=views.AnimalDetail.name),

    path('reservation', views.ReservationList.as_view(), name=views.ReservationList.name),
    path('reservation/<int:pk>', views.ReservationDetail.as_view(), name=views.ReservationDetail.name),

    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

]