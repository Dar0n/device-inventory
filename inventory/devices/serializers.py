
from rest_framework import serializers

from inventory.customers.serializers import CustomerSerializer
from inventory.models import Device, LoRaWAN, DeviceModel, DeviceConfigurationFieldValue


class DeviceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()


    class Meta:
        model = Device
        fields = '__all__'

    def create(self, validated_data):
        lorawan = LoRaWAN.objects.create(

        )
        device_model = DeviceModel.objects.get(pk=self.context['device_model_id'])
        device = Device.objects.create(
            name = validated_data.get('name'),
            date_of_delivery = validated_data.get('date_of_delivery'),
            serial_number = validated_data.get('serial_number'),
            firmware_version = validated_data.get('firmware_version'),
            hardware_version = validated_data.get('hardware_version'),
            customer = validated_data.get('customer'),
            lorawan = lorawan,
            device_model = device_model,
        )

        return device