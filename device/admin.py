from django.contrib import admin
from django.http import HttpResponse
from .models import Zone, Device, Sensor, CombinedView, SensorHistory
import csv


class ZoneAdmin(admin.ModelAdmin):
    list_filter = ["name"]
    list_display = ("name", "get_device_id")
    search_fields = ["name"]
    actions = ['export']

    def get_device_id(self, obj):
        return obj.devices.device_id
    get_device_id.short_description = 'Device ID'

    def export(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="Zone.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(["name", "device_id"])
        for zone in queryset:
            writer.writerow([zone.name, zone.devices.device_id])
        return response


class DeviceAdmin(admin.ModelAdmin):
    list_filter = ["device_id"]
    list_display = ("device_id", "description", "status",
                    "get_sensor")
    search_fields = ["device_id"]
    actions = ['export']

    def get_sensor(self, obj):
        return obj.sensors.sensor_id
    get_sensor.short_description = 'Sensor'

    def export(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="Device.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(
            ["device_id", "status", "description", "sensor"])
        for device in queryset:
            writer.writerow([device.device_id,
                            device.description, device.status, device.sensors.sensor_id])
        return response


class SensorAdmin(admin.ModelAdmin):
    list_filter = ["sensor_id"]
    list_display = ("sensor_id", "sensor_type", "value")
    search_fields = ["sensor_id"]
    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="Sensor.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(["sensor_id", "sensor_type", "value"])
        for sensor in queryset:
            writer.writerow(
                [sensor.sensor_id, sensor.sensor_type, sensor.value])
        return response


@admin.register(SensorHistory)
class SensorHistoryAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'value', 'timestamp', 'modified_at')
    search_fields = ('sensor__sensor_id', 'value')
    list_filter = ('timestamp', 'modified_at')
    actions = ['export']

    def export(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": 'attachment; filename="Sensor History.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(["sensor", "value", "timestamp", "modified_at"])
        for sensor in queryset:
            writer.writerow(
                [sensor.sensor_id, sensor.value, sensor.timestamp, sensor.modified_at])
        return response


class CombinedAdmin(admin.ModelAdmin):
    list_display = ("sensor_id", "device_id", "zone_name",
                    "sensor_type", "sensor_value", "device_description", "status")

    search_fields = ["zone__name", "device__device_id", "sensor__sensor_id"]
    actions = ['export']

    def get_queryset(self, request):
        queryset = Zone.objects.all().select_related('devices__sensors')
        return queryset

    def zone_name(self, obj):
        return obj.name
    zone_name.short_description = 'Zone Name'

    def device_id(self, obj):
        return obj.devices.device_id
    device_id.short_description = 'Device ID'

    def device_description(self, obj):
        return obj.devices.description
    device_description.short_description = 'Device Description'

    def status(self, obj):
        return obj.devices.status
    status.short_description = 'Status'

    def sensor_id(self, obj):
        return obj.devices.sensors.sensor_id
    sensor_id.short_description = 'Sensor ID'

    def sensor_type(self, obj):
        return obj.devices.sensors.sensor_type
    sensor_type.short_description = 'Sensor Type'

    def sensor_value(self, obj):
        return obj.devices.sensors.value
    sensor_value.short_description = 'Sensor Value'

    def export(self, request, queryset):
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="Combined.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(["Sensor ID", "Device ID", "Zone Name",
                        "Sensor Type", "Sensor Value", "Device Description", "Status"])
        for obj in queryset:
            writer.writerow([obj.devices.sensors.sensor_id,
                             obj.devices.device_id,
                             obj.name,
                             obj.devices.sensors.sensor_type,
                             obj.devices.sensors.value,
                             obj.devices.description,
                             obj.devices.status])
        return response


admin.site.register(Zone, ZoneAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(CombinedView, CombinedAdmin)
