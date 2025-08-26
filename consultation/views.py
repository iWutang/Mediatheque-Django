from django.shortcuts import render
from gestion.models import Media

# Create your views here.

def liste_medias(request):
    medias = Media.objects.exclude(type_media="jeu")
    return render(request, "consultation/liste_medias.html", {"medias": medias})