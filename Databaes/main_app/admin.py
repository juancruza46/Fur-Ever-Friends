from django.contrib import admin
from .models import Pet, Appointment, Photo

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('pet', 'date', 'time')
    list_filter = ('date', 'time')
    search_fields = ('pet__name',)

admin.site.register(Pet)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Photo)