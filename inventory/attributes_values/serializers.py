from rest_framework import serializers

from inventory.configuration_fields.serializers import ConfigurationFieldSerializer
from inventory.devices.serializers import DeviceSerializer
from inventory.models import DeviceConfigurationFieldValue, ConfigurationField, Device


class AttributeValueSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    configuration_field = ConfigurationFieldSerializer(read_only=True)

    class Meta:
        model = DeviceConfigurationFieldValue
        fields = '__all__'

    def create(self, validated_data):
        device = Device.objects.get(pk=self.context['device_id'])
        configuration_field = ConfigurationField.objects.get(pk=self.context['configuration_field_id'])
        attribute_value = DeviceConfigurationFieldValue.objects.create(
            value = validated_data.get('value'),
            configuration_field = configuration_field,
            device = device,
        )

        return attribute_value