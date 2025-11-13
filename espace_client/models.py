from django.db import models
from django.contrib.auth.models import User


class ClientMaghrebia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    cin = models.CharField(max_length=8, unique=True, verbose_name="CIN")
    telephone = models.CharField(max_length=12, verbose_name="Téléphone")
    adresse = models.TextField(verbose_name="Adresse")
    date_inscription = models.DateField(auto_now_add=True, verbose_name="Date d'inscription")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class PoliceMaghrebia(models.Model):
    TYPE_CHOICES = [
        ('auto', 'Assurance Auto (RC + Tous Risques)'),
        ('sante', 'Assurance Santé (Médiplus, etc.)'),
        ('habitation', 'Assurance Habitation'),
        ('voyage', 'Assurance Voyage'),
    ]

    client = models.ForeignKey(ClientMaghrebia, on_delete=models.CASCADE, related_name='polices')
    numero_police = models.CharField(max_length=20, unique=True, verbose_name="Numéro de police")
    type_assurance = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Type d'assurance")
    date_effet = models.DateField(verbose_name="Date d'effet")
    date_expiration = models.DateField(verbose_name="Date d'expiration")
    prime_mensuelle = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prime mensuelle")
    est_active = models.BooleanField(default=True, verbose_name="Active")

    def __str__(self):
        return f"{self.numero_police} - {self.get_type_assurance_display()}"

    class Meta:
        verbose_name = "Police"
        verbose_name_plural = "Polices"


class SinistreMaghrebia(models.Model):
    STATUT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('en_investigation', 'En investigation'),
        ('expertise_en_cours', 'Expertise en cours'),
        ('indemnise', 'Indemnisé'),
        ('rejete', 'Rejeté'),
    ]

    police = models.ForeignKey(PoliceMaghrebia, on_delete=models.CASCADE, related_name='sinistres')
    date_sinistre = models.DateField(verbose_name="Date du sinistre")
    lieu = models.CharField(max_length=200, verbose_name="Lieu")
    description = models.TextField(verbose_name="Description")
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='nouveau',
        verbose_name="Statut"
    )
    montant_indemnite = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Montant de l'indemnité"
    )
    date_traitement = models.DateField(null=True, blank=True, verbose_name="Date de traitement")

    def __str__(self):
        return f"Sinistre {self.id} - Police {self.police.numero_police}"

    class Meta:
        verbose_name = "Sinistre"
        verbose_name_plural = "Sinistres"