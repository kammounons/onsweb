
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'doctor',
        'appointment_date',
        'status',
        'duration_minutes',
    )

    search_fields = (
        'patient__last_name',
        'patient__first_name',
        'doctor__last_name',
        'doctor__first_name',
        'status',
    )

    ordering = ('appointment_date',)
