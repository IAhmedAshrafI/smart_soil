from django.contrib import admin
from django.urls import path, include
from .views import ZoneLevel
from .views import ZoneLevel, ExportToCsv

urlpatterns = [
    path("device/<str:level1>/<str:level2>/<str:level3>/<str:level4>/<str:level5>/<str:level6>/<str:level7>/<str:level8>/<str:level9>/<str:level10>/", ZoneLevel.as_view(), name="zone-level")
]
    path("device/<str:level1>/<str:level2>/<str:level3>/<str:level4>/<str:level5>/<str:level6>/<str:level7>/<str:level8>/<str:level9>/<str:level10>/",
         ZoneLevel.as_view(), name="zone-level"),
    path("exportcsv/", ExportToCsv.as_view(), name="exportcsv")
]
