from django.urls import path
from . import views

app_name = "sinistre"

urlpatterns = [
    path("", views.liste_sinistres, name="liste_sinistres"),
    path("declarer/", views.declarer_sinistre, name="declarer_sinistre"),
]
