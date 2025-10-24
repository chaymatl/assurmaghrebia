from django import forms
from .models import Sinistre

class SinistreForm(forms.ModelForm):
    class Meta:
        model = Sinistre
        fields = ["type_sinistre", "description", "montant_demande"]
        widgets = {
            "description": forms.Textarea(attrs={"rows":4}),
        }
