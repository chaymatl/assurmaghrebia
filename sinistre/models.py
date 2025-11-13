# sinistre/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
User = settings.AUTH_USER_MODEL


class Sinistre(models.Model):
    class StatutChoices(models.TextChoices):
        EN_COURS = 'en_cours', _('En cours')
        CLOS = 'clos', _('Clos')
        REFUSE = 'refuse', _('Refusé')

    class TypeSinistreChoices(models.TextChoices):
        AUTOMOBILE = 'automobile', _('Automobile')
        HABITATION = 'habitation', _('Habitation')
        SANTE = 'sante', _('Santé')
        AUTRE = 'autre', _('Autre')

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sinistres",
        verbose_name=_("Client")
    )
    titre = models.CharField(
        max_length=200,
        verbose_name=_("Titre"),
        help_text=_("Ex: Dégât des eaux - Appartement Tunis")
    )
    date_declaration = models.DateTimeField(
    default=timezone.now,
    verbose_name=_("Date de déclaration")
)
    type_sinistre = models.CharField(
        max_length=20,
        choices=TypeSinistreChoices.choices,
        verbose_name=_("Type de sinistre")
    )
    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Décrivez les circonstances du sinistre")
    )
    statut = models.CharField(
        max_length=20,
        choices=StatutChoices.choices,
        default=StatutChoices.EN_COURS,
        verbose_name=_("Statut")
    )
    montant_demande = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Montant demandé")
    )
    montant_indemnisation = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name=_("Montant d'indemnisation")
    )

    class Meta:
        verbose_name = _("Sinistre")
        verbose_name_plural = _("Sinistres")
        ordering = ['-date_declaration']
    justificatif = models.FileField(upload_to='sinistres/', blank=True, null=True, verbose_name="Justificatif")

    def __str__(self):
        return f"Sinistre #{self.id} - {self.titre}"

    @property
    def est_cloture(self):
        return self.statut == self.StatutChoices.CLOS