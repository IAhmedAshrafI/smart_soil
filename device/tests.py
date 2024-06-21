
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Sensor, Device


class SensorDetailsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_sensor(self):
        url = reverse('sensordetails', args=["123", 20])

        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        sensor = Sensor.objects.get(sensor_id="123")
        self.assertEqual(sensor.value, 20)
        self.assertIsNone(sensor.sensor_type)

        self.assertEqual(response.data, {"created": "success!"})
