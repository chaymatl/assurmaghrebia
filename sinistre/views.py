from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

from .models import Sinistre
from .forms import SinistreForm


@login_required
def liste_sinistres(request):
    if request.user.is_superuser:
        sinistres = Sinistre.objects.all().order_by('-date_declaration')
        template = "sinistre/liste_admin.html"
    else:
        sinistres = Sinistre.objects.filter(client=request.user).order_by('-date_declaration')
        template = "sinistre/liste.html"
    
    return render(request, template, {
        "sinistres": sinistres,
        "titre_page": _("Mes sinistres")
    })


@login_required
def declarer_sinistre(request):
    if request.method == "POST":
        form = SinistreForm(request.POST)
        if form.is_valid():
            sinistre = form.save(commit=False)
            sinistre.client = request.user
            sinistre.save()
            messages.success(request, _("Votre sinistre a été déclaré avec succès."))
            return redirect("sinistre:liste_sinistres")
    else:
        form = SinistreForm()
    
    return render(request, "sinistre/declarer.html", {
        "form": form,
        "titre_page": _("Déclarer un sinistre")
    })


@login_required
def detail_sinistre(request, pk):
    sinistre = get_object_or_404(Sinistre, pk=pk)
    if not (request.user.is_superuser or sinistre.client == request.user):
        raise PermissionDenied

    if request.method == "POST":
        sinistre.titre = request.POST.get('titre', sinistre.titre)
        sinistre.client_id = int(request.POST.get('client'))
        sinistre.type_sinistre = request.POST.get('type_sinistre', sinistre.type_sinistre)
        sinistre.statut = request.POST.get('statut', sinistre.statut)
        sinistre.description = request.POST.get('description', sinistre.description)
        sinistre.montant_demande = request.POST.get('montant_demande') or None
        sinistre.montant_indemnisation = request.POST.get('montant_indemnisation') or None

        from django.utils import timezone
        try:
            new_date = timezone.datetime.fromisoformat(request.POST.get('date_declaration'))
            sinistre.date_declaration = new_date
        except (ValueError, TypeError):
            messages.error(request, "Date invalide.")
            return render(request, "sinistre/detail.html", {
                "sinistre": sinistre,
                "users": User.objects.all(),
                "type_choices": Sinistre.TypeSinistreChoices.choices,
                "statut_choices": Sinistre.StatutChoices.choices,
                "titre_page": _("Détails du sinistre #%(id)s") % {'id': sinistre.id}
            })

        sinistre.save()
        messages.success(request, "Les modifications ont été sauvegardées.")
        return redirect("sinistre:liste_sinistres")

    return render(request, "sinistre/detail.html", {
        "sinistre": sinistre,
        "users": User.objects.all(),
        "type_choices": Sinistre.TypeSinistreChoices.choices,
        "statut_choices": Sinistre.StatutChoices.choices,
        "titre_page": _("Détails du sinistre #%(id)s") % {'id': sinistre.id}
    })


def accueil(request):
    return render(request, 'acceuil.html')  