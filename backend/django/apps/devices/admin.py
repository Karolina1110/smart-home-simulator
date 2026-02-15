from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "device_type", "location", "is_active", "created_at")
    list_filter = ("device_type", "is_active")
    search_fields = ("name", "location")