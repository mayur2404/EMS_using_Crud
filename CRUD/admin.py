from django.contrib import admin
from .models import *

# Register your models here.

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["name","email","address","phone",]

admin.site.register(Employees)