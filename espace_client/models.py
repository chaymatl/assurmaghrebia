from django.db import models
from django.contrib.auth.models import User

class ClientMaghrebia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cin = models.CharField(max_length=8, unique=True, verbose_name="CIN")
    telephone = models.CharField(max_length=12)
    adresse = models.TextField()
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class PoliceMaghrebia(models.Model):
    TYPE_CHOICES = [
        ('auto', 'Assurance Auto (RC + Tous Risques)'),
        ('sante', 'Assurance Santé (Médiplus, etc.)'),
        ('habitation', 'Assurance Habitation'),
        ('voyage', 'Assurance Voyage'),
    ]
    client = models.ForeignKey(ClientMaghrebia, on_delete=models.CASCADE)
    numero_police = models.CharField(max_length=20, unique=True)  # ex: MA-2025-12345
    type_assurance = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_effet = models.DateField()
    date_expiration = models.DateField()
    prime_mensuelle = models.DecimalField(max_digits=10, decimal_places=2)
    est_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.numero_police} - {self.get_type_assurance_display()}"

class SinistreMaghrebia(models.Model):
    police = models.ForeignKey(PoliceMaghrebia, on_delete=models.CASCADE)
    date_sinistre = models.DateField()
    lieu = models.CharField(max_length=200)
    description = models.TextField()
    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('en_investigation', 'En investigation'),
        ('expertise_en_cours', 'Expertise en cours'),
        ('indemnise', 'Indemnisé'),
        ('rejete', 'Rejeté'),
    ]
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouveau')
    montant_indemnite = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_traitement = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Sinistre {self.id} - Police {self.police.numero_police}"