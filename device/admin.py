from django.contrib import admin
from django.http import HttpResponse
from .models import Zone, Zone_History
import csv


class ZoneHistoryAdmin(admin.ModelAdmin):
    list_filter = [
         "zone",
        "zone",
    ]
    list_display = ("zone", "level", "time",)
    search_fields = (
        "zone",
    )
    actions = ['export']

    def export(self, request, queryset):
        print(request)
        zone_history = queryset.all()
        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": 'attachment; filename="Zone History.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(["zone", "level", "time"])
        zone_fields = zone_history.values_list("zone", "level", "time")
        for zone in zone_fields:
            writer.writerow(zone)
        return response


class ZoneAdmin(admin.ModelAdmin):
    list_filter = [
         "name",
        "name",
    ]
    list_display = ("name", "level",)
    search_fields = (
        "name",
    )
    actions = ['export']

    def export(self, request, queryset):
        zone = queryset.all()
        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": 'attachment; filename="Zone.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(["name", "level"])
        zone_fields = zone.values_list("name", "level")
        for zone in zone_fields:
            writer.writerow(zone)
        return response


admin.site.register(Zone, ZoneAdmin)
admin.site.register(Zone_History, ZoneHistoryAdmin)
