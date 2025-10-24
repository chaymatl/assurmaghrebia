from django.contrib import admin
from .models import Sinistre

@admin.register(Sinistre)
class SinistreAdmin(admin.ModelAdmin):
    list_display = ("id", "client", "type_sinistre", "statut", "date_declaration")
    list_filter = ("statut", "type_sinistre")
    search_fields = ("client__username", "type_sinistre", "description")
