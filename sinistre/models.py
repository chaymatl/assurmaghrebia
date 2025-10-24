from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Sinistre(models.Model):
    STATUTS = [
        ("en_cours", "En cours"),
        ("clos", "Clos"),
        ("refuse", "Refusé"),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sinistres")
    date_declaration = models.DateTimeField(auto_now_add=True)
    type_sinistre = models.CharField(max_length=100)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUTS, default="en_cours")
    montant_demande = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    montant_indemnisation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Sinistre #{self.id} - {self.client} - {self.get_statut_display()}"
