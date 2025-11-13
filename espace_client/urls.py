from django.urls import path
from . import views

app_name = 'espace_client'

urlpatterns = [
    path('', views.espace_client_accueil, name='accueil'),
]