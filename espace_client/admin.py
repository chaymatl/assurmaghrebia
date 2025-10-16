from django.contrib import admin
from .models import ClientMaghrebia, PoliceMaghrebia, SinistreMaghrebia

@admin.register(ClientMaghrebia)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'cin', 'telephone']

@admin.register(PoliceMaghrebia)
class PoliceAdmin(admin.ModelAdmin):
    list_display = ['numero_police', 'client', 'type_assurance', 'date_expiration', 'est_active']
    list_filter = ['type_assurance', 'est_active']

@admin.register(SinistreMaghrebia)
class SinistreAdmin(admin.ModelAdmin):
    list_display = ['id', 'police', 'date_sinistre', 'statut']
    list_filter = ['statut', 'date_sinistre']