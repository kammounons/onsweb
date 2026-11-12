
from django.db import models
from Cabinet.models import Medecin, Patient


class RendezVous(models.Model):

    class Statut(models.TextChoices):
        EN_ATTENTE = 'EN_ATTENTE', 'En attente'
        CONFIRME = 'CONFIRME', 'Confirmé'
        ANNULE = 'ANNULE', 'Annulé'

    motif = models.TextField()

    ordonnance = models.FileField(
        upload_to='ordonnances/',
        blank=True,
        null=True
    )

    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE
    )

    duree_minutes = models.IntegerField(default=30)

    date_rdv = models.DateTimeField()

    date_creation = models.DateTimeField(auto_now_add=True)

    date_maj = models.DateTimeField(auto_now=True)

    medecin = models.ForeignKey(
        Medecin,
        on_delete=models.CASCADE,
        related_name='rendezvous'
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='rendezvous'
    )

    def __str__(self):
        return f"{self.patient} - {self.medecin}"
