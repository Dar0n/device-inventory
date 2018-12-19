from rest_framework import serializers

from inventory.configuration_fields.serializers import ConfigurationFieldSerializer
from inventory.devices.serializers import DeviceSerializer
from inventory.models import DeviceModel, Device


class DeviceModelSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True)
    configuration_fields = ConfigurationFieldSerializer(many=True)

    class Meta:
        model = DeviceModel
        fields = '__all__'

    def create(self, validated_data):
        device_model = DeviceModel.objects.create(
            name = validated_data.get('name'),
        )

        return device_model