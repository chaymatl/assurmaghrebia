# sinistre/admin.py
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Sinistre


@admin.register(Sinistre)
class SinistreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titre',
        'client',
        'type_sinistre',
        'statut',
        'date_declaration',
    )
    list_display_links = ('id',)
    
    # ✅ Rendre ces champs éditables DIRECTEMENT dans la liste
    list_editable = ('titre', 'client', 'statut', 'date_declaration')
    
    list_filter = ('statut', 'type_sinistre', 'date_declaration')
    search_fields = ('titre', 'description', 'client__username', 'client__email')
    date_hierarchy = 'date_declaration'

    fieldsets = (
        (_("Informations client"), {
            'fields': ('client', 'date_declaration')
        }),
        (_("Détails du sinistre"), {
            'fields': ('titre', 'type_sinistre', 'description')
        }),
        (_("Traitement"), {
            'fields': ('statut', 'montant_demande', 'montant_indemnisation')
        }),
    )

    # --- Actions utiles (optionnelles mais conservées) ---
    actions = [
        'marquer_comme_clos',
        'marquer_comme_refuse',
        'marquer_comme_en_cours',
        'changer_type_automobile',
        'changer_type_habitation',
        'changer_type_sante',
        'changer_type_autre',
    ]

    # --- Actions Statut ---
    def marquer_comme_clos(self, request, queryset):
        updated = queryset.update(statut=Sinistre.StatutChoices.CLOS)
        self.message_user(request, _("{} sinistre(s) marqué(s) comme Clos.").format(updated))
    marquer_comme_clos.short_description = _("Marquer comme Clos")

    def marquer_comme_refuse(self, request, queryset):
        updated = queryset.update(statut=Sinistre.StatutChoices.REFUSE)
        self.message_user(request, _("{} sinistre(s) marqué(s) comme Refusé.").format(updated))
    marquer_comme_refuse.short_description = _("Marquer comme Refusé")

    def marquer_comme_en_cours(self, request, queryset):
        updated = queryset.update(statut=Sinistre.StatutChoices.EN_COURS)
        self.message_user(request, _("{} sinistre(s) remis en cours.").format(updated))
    marquer_comme_en_cours.short_description = _("Remettre en cours")

    # --- Actions Type Sinistre ---
    def changer_type_automobile(self, request, queryset):
        updated = queryset.update(type_sinistre=Sinistre.TypeSinistreChoices.AUTOMOBILE)
        self.message_user(request, _("{} sinistre(s) changé(s) en Automobile.").format(updated))
    changer_type_automobile.short_description = _("Changer le type en Automobile")

    def changer_type_habitation(self, request, queryset):
        updated = queryset.update(type_sinistre=Sinistre.TypeSinistreChoices.HABITATION)
        self.message_user(request, _("{} sinistre(s) changé(s) en Habitation.").format(updated))
    changer_type_habitation.short_description = _("Changer le type en Habitation")

    def changer_type_sante(self, request, queryset):
        updated = queryset.update(type_sinistre=Sinistre.TypeSinistreChoices.SANTE)
        self.message_user(request, _("{} sinistre(s) changé(s) en Santé.").format(updated))
    changer_type_sante.short_description = _("Changer le type en Santé")

    def changer_type_autre(self, request, queryset):
        updated = queryset.update(type_sinistre=Sinistre.TypeSinistreChoices.AUTRE)
        self.message_user(request, _("{} sinistre(s) changé(s) en Autre.").format(updated))
    changer_type_autre.short_description = _("Changer le type en Autre")