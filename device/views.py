from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Zone, Zone_History
from datetime import datetime




class ZoneLevel(APIView):
    def get(self, request, **kwargs):
        zones = Zone.objects.all()

        error = {"error", "failed"}
        if not zones and len(zones) < 10 :
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if len(list(kwargs.values())) < 10:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        for value, zone in zip(kwargs.values(), zones):
            zone.level=value
            zone_history = Zone_History()
            zone_history.zone = zone
            zone_history.level=value
            zone_history.time = datetime.now()
            zone.save()
            zone_history.save()
        data={"created":"success!"}
        return Response(data, status=status.HTTP_200_OK)

