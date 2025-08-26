from django.urls import path
from . import views

urlpatterns = [
    # Membres
    path("membres/", views.liste_membres, name="liste_membres"),
    path("membres/ajouter/", views.ajouter_membre, name="ajouter_membre"),
    path("membres/<int:membre_id>/modifier/", views.modifier_membre, name="modifier_membre"),

    # Médias
    path("medias/", views.liste_medias, name="liste_medias"),
    path("medias/ajouter/", views.ajouter_media, name="ajouter_media"),

    # Emprunts
    path("emprunts/creer/", views.creer_emprunt, name="creer_emprunt"),
    path("emprunts/<int:emprunt_id>/retour/", views.retour_emprunt, name="retour_emprunt"),
]