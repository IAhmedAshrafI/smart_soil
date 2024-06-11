from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=255)
    devices = models.ForeignKey(
        'Device', related_name='zones', on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name


class Device(models.Model):
    device_id = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    sensors = models.ForeignKey(
        'Sensor', related_name='devices', on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.device_id


class Sensor(models.Model):
    sensor_id = models.CharField(max_length=255, primary_key=True)
    sensor_type = models.CharField(max_length=255)
    value = models.IntegerField()

    def __str__(self) -> str:
        return self.sensor_id


class CombinedView(models.Model):
    class Meta:
        managed = False  # No migrations will be created for this model
        verbose_name = 'Combined View'
        verbose_name_plural = 'Combined Views'
