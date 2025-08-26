from django.contrib import admin
from .models import Membre, Media, Emprunt

# Register your models here.

@admin.register(Membre)
class MembreAdmin(admin.ModelAdmin):
    list_display = ("nom", "bloque", "nb_emprunts")

    def nb_emprunts(self, obj):
        return obj.emprunts_actifs().count()
    nb_emprunts.short_description = "Emprunts actifs"


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("titre", "type_media", "disponible")
    list_filter = ("type_media", "disponible")


@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ("membre", "media", "date_emprunt", "retourne", "en_retard")

    def en_retard(self, obj):
        return obj.est_en_retard()
    en_retard.boolean = True
    en_retard.short_description = "En retard ?"
