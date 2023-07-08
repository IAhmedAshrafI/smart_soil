from rest_framework import status
from .models import Zone, Zone_History
from datetime import datetime


from django.http import HttpResponse
import csv


class ZoneLevel(APIView):
    def get(self, request, **kwargs):
        zones = Zone.objects.all()

        error = {"error", "failed"}
        if not zones and len(zones) < 10 :
        if not zones and len(zones) < 10:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if len(list(kwargs.values())) < 10:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        for value, zone in zip(kwargs.values(), zones):
            zone.level=value
            zone.level = value
            zone_history = Zone_History()
            zone_history.zone = zone
            zone_history.level=value
            zone_history.level = value
            zone_history.time = datetime.now()
            zone.save()
            zone_history.save()
        data={"created":"success!"}
        data = {"created": "success!"}
        return Response(data, status=status.HTTP_200_OK)


class ExportToCsv(APIView):
    def get(self, request, **kwargs):
        zone_history = Zone_History.objects.all()
        response = HttpResponse(
            content_type="text/csv",
            headers={
                "Content-Disposition": 'attachment; filename="somefilename.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(["zone", "level", "time"])
        zone_fields = zone_history.values_list("zone", "level", "time")
        for zone in zone_fields:
            writer.writerow(zone)
        return response
