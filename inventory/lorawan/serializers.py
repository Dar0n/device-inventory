from rest_framework import serializers

from inventory.models import LoRaWAN


class LoRaWANSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoRaWAN
        fields = '__all__'

    def create(self, validated_data):
        lorawan = LoRaWAN.objects.create(
            DevEUI = validated_data.get('DevEUI'),
            activation_type = validated_data.get('activation_type'),
            app_eui = validated_data.get('app_eui'),
            app_key = validated_data.get('app_key'),
            nwkskey = validated_data.get('nwkskey'),
            appskey = validated_data.get('appskey'),
            devaddr = validated_data.get('devaddr'),
            adr = validated_data.get('adr'),
            data_rate = validated_data.get('data_rate'),
        )

        return lorawan