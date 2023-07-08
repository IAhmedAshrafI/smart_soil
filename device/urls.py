from django.contrib import admin
from django.urls import path, include
from .views import ZoneLevel, ExportToCsv

urlpatterns = [
    path("device/<str:level1>/<str:level2>/<str:level3>/<str:level4>/<str:level5>/<str:level6>/<str:level7>/<str:level8>/<str:level9>/<str:level10>/"
         <str:level11>/<str:level12>/<str:level13>/<str:level14>/<str:level15>/<str:level16>/<str:level17>/<str:level18>/<str:level19>/<str:level20>/,
         ZoneLevel.as_view(), name="zone-level"),
    path("exportcsv/", ExportToCsv.as_view(), name="exportcsv")
]
