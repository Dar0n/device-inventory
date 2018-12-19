from django.contrib import admin

# Register your models here.
from inventory.models import Device, LoRaWAN, Customer, DeviceModel, ConfigurationField, DeviceConfigurationFieldValue

admin.site.register(Device)
admin.site.register(LoRaWAN)
admin.site.register(Customer)
admin.site.register(DeviceModel)
admin.site.register(ConfigurationField)
admin.site.register(DeviceConfigurationFieldValue)
