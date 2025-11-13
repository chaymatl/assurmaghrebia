from django.contrib import admin
from .models import ClientMaghrebia, PoliceMaghrebia, SinistreMaghrebia

@admin.register(ClientMaghrebia)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'cin', 'telephone', 'date_inscription')
    search_fields = ('user__username', 'cin', 'telephone')

@admin.register(PoliceMaghrebia)
class PoliceAdmin(admin.ModelAdmin):
    list_display = ('numero_police', 'client', 'type_assurance', 'date_effet', 'est_active')
    list_filter = ('type_assurance', 'est_active')
    search_fields = ('numero_police', 'client__cin')

@admin.register(SinistreMaghrebia)
class SinistreAdmin(admin.ModelAdmin):
    list_display = ('id', 'police', 'date_sinistre', 'statut', 'montant_indemnite')
    list_filter = ('statut', 'date_sinistre')
    search_fields = ('police__numero_police', 'lieu')