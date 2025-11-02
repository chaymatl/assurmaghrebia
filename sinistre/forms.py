# sinistre/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Sinistre

class SinistreForm(forms.ModelForm):
    class Meta:
        model = Sinistre
        fields = ["titre", "type_sinistre", "description", "montant_demande"]
        widgets = {
            "titre": forms.TextInput(attrs={"class": "form-control", "placeholder": _("Ex: Accident voiture - Ariana")}),
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "type_sinistre": forms.Select(attrs={"class": "form-control"}),
            "montant_demande": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }
        labels = {
            "titre": _("Titre du sinistre"),
            "type_sinistre": _("Type de sinistre"),
            "description": _("Description"),
            "montant_demande": _("Montant demandé (en DT)"),
        }
    
    def clean_montant_demande(self):
        montant = self.cleaned_data.get('montant_demande')
        if montant and montant <= 0:
            raise forms.ValidationError(_("Le montant doit être positif."))
        return montant