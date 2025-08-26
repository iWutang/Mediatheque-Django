from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Membre, Media, Emprunt
from .forms import MembreForm, MediaForm, EmpruntForm

# Create your views here.

#-- Membres --
def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, "gestion/liste_membres.html", {"membres": membres})

def ajouter_membre(request):
    if request.method == "POST":
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Membre ajouté avec succès !")
            return redirect("liste_membres")
        else:
            form = MembreForm()
            return render(request, "gestion/form.html", {"form": form, "title": "Ajouter un membre"})

def modifier_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    if request.method == "POST":
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            messages.success("Membre mis à jour !")
            return redirect("liste_membres")
        else:
            form = MembreForm(instance=membre)
            return render(request, "gestion/form.html", {"form": form, "title": "Modifier un membre"})

# -- Medias --

def liste_medias(request):
    medias = Media.objects.all()
    return render(request, "gestion/liste_medias.html", {"medias": medias})

def ajouter_media(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            media = form.save(commit=False)
            media.disponible = True
            media.save()
            messages.success(request, "Média ajouté avec succès !")
            return redirect("liste_medias")
        else:
            form = MediaForm()
            return render(request, "gestion/form.html", {"form": form, "title": "Ajouter un media"})

# -- Emprunts --

def creer_emprunt(request):
    if request.method == "POST":
        form = EmpruntForm(request.POST)
        if form.is_valid():
            emprunt = form.save(commit=False)
            emprunt.media.disponible = False
            emprunt.media.save()
            emprunt.save()
            messages.success(request, "Emprunt enregistré !")
            return redirect("liste_medias")
        else:
            form = EmpruntForm()
        return render(request, "gestion/form.html", {"form": form, "title": "Creer un emprunt"})

def retour_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, id=emprunt_id)
    emprunt.retourne = True
    emprunt.media.disponible = True
    emprunt.media.save()
    emprunt.save()
    messages.success(request, "Média retourné avec succès.")
    return redirect("liste_medias")