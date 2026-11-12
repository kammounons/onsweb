
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name="cabinet_users",
        related_query_name="cabinet_user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="cabinet_users",
        related_query_name="cabinet_user",
    )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"


class Specialite(models.Model):
    nom_specialite = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Spécialité"
        verbose_name_plural = "Spécialités"

    def __str__(self):
        return self.nom_specialite


class Medecin(User):
    matricule_ordre = models.CharField(max_length=6, unique=True)
    telephone = models.CharField(max_length=8)
    specialites = models.ManyToManyField(Specialite)

    class Meta:
        verbose_name = "Médecin"
        verbose_name_plural = "Médecins"

    def __str__(self):
        return self.username


class Patient(User):
    cin = models.CharField(max_length=8, unique=True)
    telephone = models.CharField(max_length=8)
    date_naissance = models.DateField()

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.username
