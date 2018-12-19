from rest_framework import serializers

from inventory.models import ConfigurationField, DeviceModel


class ConfigurationFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConfigurationField
        fields = '__all__'

    def create(self, validated_data):
        device_model = DeviceModel.objects.get(pk=self.context['device_model_id'])
        configuration_field = ConfigurationField.objects.create(
            name = validated_data.get('name'),
            type = validated_data.get('type'),
            device_model = device_model,
        )

        return configuration_field