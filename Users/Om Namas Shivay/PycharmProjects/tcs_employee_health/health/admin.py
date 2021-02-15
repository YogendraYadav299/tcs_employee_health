from django.contrib import admin
from .models import HealthReport,EmployeeDevice
# Register your models here.
admin.site.register(EmployeeDevice)
admin.site.register(HealthReport)