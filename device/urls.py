from django.contrib import admin
from django.urls import path, include
from .views import ExportToCsv, SensorDetails, SetDeviceFlag

urlpatterns = [
    # path("device/<str:level1>/<str:level2>/<str:level3>/<str:level4>/<str:level5>/<str:level6>/<str:level7>/<str:level8>/<str:level9>/<str:level10>/",
    #      ZoneLevel.as_view(), name="zone-level"),
    # path("device/<str:number>/", GetNumber.as_view(), name="get_number"),
    path("exportcsv/", ExportToCsv.as_view(), name="exportcsv"),
    path("sensordetails/<str:pk>/<int:pk1>",
         SensorDetails.as_view(), name="sensordetails"),
    path("setdeviceflag/<str:pk>/<int:pk1>",
         SetDeviceFlag.as_view(), name="setdeviceflag")
]
