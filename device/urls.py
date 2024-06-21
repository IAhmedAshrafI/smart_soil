from django.contrib import admin
from django.urls import path, include
from .views import ExportToCsv, SensorDetails, SetDeviceFlag

urlpatterns = [
    path("exportcsv/", ExportToCsv.as_view(), name="exportcsv"),
    path("sensordetails/<str:pk>/<int:pk1>",
         SensorDetails.as_view(), name="sensordetails"),
    path("setdeviceflag/<str:pk>/<int:pk1>",
         SetDeviceFlag.as_view(), name="setdeviceflag")
]
