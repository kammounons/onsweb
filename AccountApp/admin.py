
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from AppointmentApp.models import Appointment
from .models import User, Doctor, Patient, Specialty

# SPECIALTY ADMIN

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)



# DOCTOR ADMIN


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'license_number',
        'phone',
    )

    search_fields = ('specialities',)
    ordering = ('last_name',)


# APPOINTMENT INLINE


class AppointmentInline(admin.TabularInline):
    model = Appointment
    fk_name = 'patient'
    extra = 0
    show_change_link = True

    fields = (
        'doctor',
        'appointment_date',
        'status',
        'duration_minutes',
        'reason',
    )

    ordering = ('appointment_date',)



# PATIENT ADMIN


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'birth_date',
        'phone',
    )

    search_fields = (
        'last_name',
        'first_name',
        'national_id',
    )

    ordering = ('last_name',)

    def get_inlines(self, request, obj=None):
        if obj is not None:
            return [AppointmentInline]
        return []



# USER ADMIN

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations personnelles', {
            'fields': (
                'first_name',
                'last_name',
                'email',
            ),
        }),
    )
