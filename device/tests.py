from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Zone, Zone_History


class ZoneLevelTestCase(TestCase):
    def setUp(self):
        self.url = reverse('zone-level', args=['value1', 'value2', 'value3',
                           'value4', 'value5', 'value6', 'value7', 'value8', 'value9', 'value10'])
        self.zone_data = {'zone1': 'value1',
                          'zone2': 'value2'}  # Example zone data
        # Example invalid zone data
        self.invalid_zone_data = {'zone1': 'value1'}

    def test_zone_level_creation(self):
        response = self.client.get(self.url, data=self.zone_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'created': 'success!'})
        # Additional assertions to check if zone levels and history are created as expected

    def test_invalid_zone_data(self):
        response = self.client.get(self.url, data=self.invalid_zone_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'failed'})
        # Additional assertions to check if no zone levels or history are created


# Assuming you have configured the URL pattern for the view as follows:
# path("device/<str:level1>/<str:level2>/<str:level3>/<str:level4>/<str:level5>/<str:level6>/<str:level7>/<str:level8>/<str:level9>/<str:level10>/", ZoneLevel.as_view(), name="zone-level")
