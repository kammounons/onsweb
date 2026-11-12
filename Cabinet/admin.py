
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

from .models import User, Specialite, Medecin, Patient


# Formulaire de création d'un médecin
class MedecinCreationForm(UserCreationForm):
    class Meta:
        model = Medecin
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "matricule_ordre",
            "telephone",
            "specialites",
        )


# Formulaire de création d'un patient
class PatientCreationForm(UserCreationForm):
    class Meta:
        model = Patient
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "cin",
            "telephone",
            "date_naissance",
        )


# Administration des médecins
class MedecinAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs["form"] = MedecinCreationForm
        return super().get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return (
                ("Informations du compte", {
                    "fields": (
                        "username",
                        "first_name",
                        "last_name",
                        "email",
                        "password1",
                        "password2",
                    )
                }),
                ("Informations du médecin", {
                    "fields": (
                        "matricule_ordre",
                        "telephone",
                        "specialites",
                    )
                }),
            )
        return super().get_fieldsets(request, obj)


# Administration des patients
class PatientAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            kwargs["form"] = PatientCreationForm
        return super().get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        if obj is None:
            return (
                ("Informations du compte", {
                    "fields": (
                        "username",
                        "first_name",
                        "last_name",
                        "email",
                        "password1",
                        "password2",
                    )
                }),
                ("Informations du patient", {
                    "fields": (
                        "cin",
                        "telephone",
                        "date_naissance",
                    )
                }),
            )
        return super().get_fieldsets(request, obj)


# Enregistrement des modèles
admin.site.register(User)
admin.site.register(Specialite)
admin.site.register(Medecin, MedecinAdmin)
admin.site.register(Patient, PatientAdmin)
