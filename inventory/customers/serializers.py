from rest_framework import serializers

from inventory.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        customer = Customer.objects.create(
            name = validated_data.get('name'),
            address = validated_data.get('address'),
            email = validated_data.get('email'),
            telephone = validated_data.get('telephone'),
        )

        return customer