from django import forms
from .models import Membre, Media, Emprunt

class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ["nom"]

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ["titre", "type_media"]

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ["membre", "media"]

    def clean(self):
        cleaned_data = super().clean()
        membre = cleaned_data.get("membre")
        media = cleaned_data.get("media")

        if media and media.type_media == "jeu":
            raise forms.ValidationError("Les jeux de plateau ne peuvent pas etre empruntés.")

        if media and not media.disponible:
            raise forms.ValidationError("Ce média n'est pas disponible.")

        if membre and not membre.peut_emprunter():
            raise forms.ValidationError("Ce membre ne peut pas emprunter (bloqué, retard ou 3 emprunts max).")

        return cleaned_data