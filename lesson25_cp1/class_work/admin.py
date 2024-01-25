from django.contrib import admin

# Register your models here.
from class_work.models import Auto

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('vin_code', 'status')

