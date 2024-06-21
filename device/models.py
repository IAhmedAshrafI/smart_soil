from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


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

    STATUS_CHOICES = [
        (0, 'Inactive'),
        (1, 'Active'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    sensors = models.ForeignKey(
        'Sensor', related_name='devices', on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.device_id


class Sensor(models.Model):
    sensor_id = models.CharField(max_length=255, primary_key=True)
    sensor_type = models.CharField(max_length=255, null=True, blank=True)
    value = models.IntegerField()

    def __str__(self) -> str:
        return self.sensor_id


class SensorHistory(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)


class CombinedView(models.Model):
    class Meta:
        managed = False
        verbose_name = 'Combined View'
        verbose_name_plural = 'Combined Views'


@receiver(post_save, sender=Sensor)
def create_or_update_sensor_history(sender, instance, created, **kwargs):
    if created:
        SensorHistory.objects.create(sensor=instance, value=instance.value)
    else:
        SensorHistory.objects.create(
            sensor=instance,
            value=instance.value,
            modified_at=timezone.now()
        )
