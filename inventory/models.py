import datetime

from django.db import models


# Create your models here.

class LoRaWAN(models.Model):
    DevEUI = models.CharField(max_length=20, blank=True, null=True)

    ACTIVATION_TYPE_OPTIONS = (
        ('OTAA', "OTAA"),
        ('ABP', "ABP")
    )

    activation_type = models.CharField(
        max_length=4,
        choices=ACTIVATION_TYPE_OPTIONS,
        blank = True,
        null=True,
    )
    app_eui = models.CharField(max_length=50, blank=True, null=True)
    app_key = models.CharField(max_length=50, blank=True, null=True)
    nwkskey = models.CharField(max_length=50, blank=True, null=True)
    appskey = models.CharField(max_length=50, blank=True, null=True)
    devaddr = models.CharField(max_length=50, blank=True, null=True)
    adr = models.BooleanField(blank=True, null=True)

    DATA_RATE_CHOICES = [(i, i) for i in range(16)]

    data_rate = models.IntegerField(
        choices=DATA_RATE_CHOICES,
        blank = True,
        null=True
    )


class DeviceModel(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name



class Customer(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    date_of_delivery = models.DateField(default=datetime.date.today, blank=True, null=True)
    serial_number = models.CharField(max_length=20, blank=True, null=True)
    firmware_version = models.CharField(max_length=50, blank=True, null=True)
    hardware_version = models.CharField(max_length=50, blank=True, null=True)
    lorawan = models.ForeignKey(
        LoRaWAN,
        on_delete=models.CASCADE,
        related_name='devices',
        blank=True, null=True
    )
    device_model = models.ForeignKey(
        DeviceModel,
        on_delete=models.CASCADE,
        related_name='devices',
        blank=True,
        null=True,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.DO_NOTHING,
        related_name='devices',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name




class ConfigurationField(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    device_model = models.ForeignKey(
        DeviceModel,
        on_delete=models.CASCADE,
        related_name='configuration_fields',
        blank=True,
        null=True,
    )

    def __str__(self):
        return "model" + self.device_model + ' ' + self.name


class DeviceConfigurationFieldValue(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE )
    configuration_field = models.ForeignKey(ConfigurationField, on_delete=models.CASCADE )
    value = models.CharField(max_length=40)

    class Meta:
        unique_together=(('device', 'configuration_field'),)

    def __str__(self):
        return 'model ' + self.device_model + ' to ' + self.configuration_field




