from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def emprunts_actifs(self):
        return self.emprunt_set.filter(retourne=False)

    def peut_emprunter(self):
        if self.bloque:
            return False
        if self.emprunts_actifs().count() >= 3:
            return False
        for e in self.emprunts_actifs():
            if e.est_en_retard():
                return False
        return True

    def __str__(self):
        return self.nom

class Media(models.Model):
    TYPES = [
        ("livre", "Livre"),
        ("dvd", "DVD"),
        ("cd", "CD"),
        ("jeu", "Jeu de plateau"),
    ]
    titre = models.CharField(max_length=200)
    type_media = models.CharField(max_length=20, choices=TYPES)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titre} ({self.get_type_media_display()})"

class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(default=timezone.now)
    retourne = models.BooleanField(default=False)

    def est_en_retard(self):
        if self.retourne:
            return False
        limite = self.date_emprunt - timedelta(days=7)
        return timezone.now() > limite

    def __str__(self):
        return f"{self.membre.nom} => {self.media.titre}"