from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ClientMaghrebia, PoliceMaghrebia, SinistreMaghrebia

@login_required
def espace_client_accueil(request):
    # Vérifie si le client existe
    try:
        client = request.user.client
    except ClientMaghrebia.DoesNotExist:
        # Option 1 : Rediriger vers une page d’erreur ou de création
        messages.error(request, "Votre profil client n’est pas encore configuré. Veuillez contacter l’administrateur.")
        return redirect('accueil')  # ou une page dédiée

    polices = PoliceMaghrebia.objects.filter(client=client)
    sinistres = SinistreMaghrebia.objects.filter(police__client=client)
    return render(request, 'espace_client/accueil.html', {
        'polices': polices,
        'sinistres': sinistres
    })