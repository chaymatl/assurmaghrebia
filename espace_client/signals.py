from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ClientMaghrebia

@receiver(post_save, sender=User)
def create_client_profile(sender, instance, created, **kwargs):
    if created:
        # Génère un CIN temporaire (à remplacer dans le formulaire d’inscription)
        cin_temp = f"TMP{instance.id:05d}"
        ClientMaghrebia.objects.create(
            user=instance,
            cin=cin_temp,
            telephone="",
            adresse=""
        )