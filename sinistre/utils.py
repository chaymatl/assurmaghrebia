# sinistre/utils.py
from django.core.mail import send_mail
from django.conf import settings

def envoyer_notification_sinistre(user_email, sujet, message):
    """
    Envoie un email simple à un utilisateur.
    """
    send_mail(
        sujet,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )