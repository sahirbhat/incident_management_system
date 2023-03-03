from django.contrib import admin
from . models import incidents

# Register your models here.

@admin.register(incidents)
class incidentsAdmin(admin.ModelAdmin):
    list_display =['incident_id','reporter_name','incident_details','reported_date_time','priority','incident_status']

