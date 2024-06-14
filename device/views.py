from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device, Sensor, CombinedView, Zone
from datetime import datetime
from django.http import HttpResponse
import csv
from django.shortcuts import get_object_or_404
from django.views import View

# class ZoneLevel(APIView):
#     def get(self, request, **kwargs):
#         zones = Zone.objects.all()

#         error = {"error", "failed"}
#         if not zones and len(zones) < 10:
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)
#         if len(list(kwargs.values())) < 10:
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)

#         for value, zone in zip(kwargs.values(), zones):
#             zone.level = value
#             zone_history = Zone_History()
#             zone_history.zone = zone
#             zone_history.level = value
#             zone_history.time = datetime.now()
#             zone.save()
#             zone_history.save()
#         data = {"created": "success!"}
#         return Response(data, status=status.HTTP_200_OK)


class SensorDetails(APIView):
    def post(self, request, pk, pk1):

        error = {"error": "failed"}
        data = {"created": "success!"}
        try:
            get_sensor = Sensor.objects.get(sensor_id=pk)

        except Sensor.DoesNotExist:
            sensor = Sensor(sensor_id=pk, value=pk1)

            if not sensor:
                return Response(error, status=status.HTTP_400_BAD_REQUEST)

            sensor.save()

            return Response(data, status=status.HTTP_201_CREATED)

        s_type = get_sensor.sensor_type
        sensor = Sensor(sensor_id=pk, sensor_type=s_type, value=pk1)
        if not sensor:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        sensor.save()
        return Response(data, status=status.HTTP_201_CREATED)


class SetDeviceFlag(APIView):
    def post(self, request, pk, pk1):
        device = get_object_or_404(Device, device_id=pk)

        if pk1 != 1 and pk1 != 0:
            return Response({"error": "Invalid flag value"}, status=status.HTTP_400_BAD_REQUEST)

        device.status = pk1
        device.save()

        data = {"created": "success!"}
        return Response(data, status=status.HTTP_201_CREATED)


class ExportToCsv(APIView):
    def get(self, request, **kwargs):
        # Fetch data from the related models
        combined_data = []
        zones = Zone.objects.all()
        for zone in zones:
            device = zone.devices
            if device:
                sensor = device.sensors
                combined_data.append({
                    'name': zone.name,
                    'device_id': device.device_id,
                    'description': device.description,
                    "status": device.status,
                    'sensor_id': sensor.sensor_id if sensor else None,
                    'sensor_type': sensor.sensor_type if sensor else None,
                    'value': sensor.value if sensor else None,
                })

        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="Combined.csv"'},
        )

        writer = csv.writer(response)
        writer.writerow(["Sensor ID", "Device ID", "Zone Name",
                        "Sensor Type", "Sensor Value", "Device Description", "Status"])

        for row in combined_data:
            writer.writerow([
                row['sensor_id'],
                row['device_id'],
                row['name'],
                row['sensor_type'],
                row['value'],
                row['description'],
                row['status']
            ])

        return response


# class ExportToCsv(APIView):
#     def get(self, request, **kwargs):
#         zone_history = Zone_History.objects.all()
#         response = HttpResponse(
#             content_type="text/csv",
#             headers={
#                 "Content-Disposition": 'attachment; filename="somefilename.csv"'},
#         )

#         writer = csv.writer(response)
#         writer.writerow(["zone", "level", "time"])
#         zone_fields = zone_history.values_list("zone", "level", "time")
#         for zone in zone_fields:
#             writer.writerow(zone)
#         return response
