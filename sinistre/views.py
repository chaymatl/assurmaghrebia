from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sinistre
from .forms import SinistreForm

@login_required
def liste_sinistres(request):
    # si user est staff on peut lister tous, sinon que les siens
    if request.user.is_staff:
        sinistres = Sinistre.objects.all().order_by("-date_declaration")
    else:
        sinistres = Sinistre.objects.filter(client=request.user).order_by("-date_declaration")
    return render(request, "sinistre/liste.html", {"sinistres": sinistres})

@login_required
def declarer_sinistre(request):
    if request.method == "POST":
        form = SinistreForm(request.POST)
        if form.is_valid():
            sin = form.save(commit=False)
            sin.client = request.user
            sin.save()
            return redirect("sinistre:liste_sinistres")
    else:
        form = SinistreForm()
    return render(request, "sinistre/declarer.html", {"form": form})
