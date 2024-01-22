from django.contrib import admin
from .models import Pet, Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'date', 'time')
    list_filter = ('date', 'time')
    search_fields = ('pet__name',)

admin.site.register(Pet)
admin.site.register(Appointment, AppointmentAdmin)