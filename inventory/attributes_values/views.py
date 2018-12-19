from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.attributes_values.serializers import AttributeValueSerializer
from inventory.configuration_fields.serializers import ConfigurationFieldSerializer
from inventory.models import ConfigurationField, DeviceConfigurationFieldValue


class PostNewAttributeValue(APIView):
    permission_classes = []

    def post(self, request, device_id, configuration_field_id):
        serializer = AttributeValueSerializer(data=request.data,
                                                  context={
                                                      "device_id": device_id,
                                                      "configuration_field_id": configuration_field_id,
                                                  }
                                                  )
        serializer.is_valid(raise_exception=True)
        attribute_value = serializer.create(serializer.validated_data)
        return Response(AttributeValueSerializer(attribute_value).data)


class GetUpdateDeleteAttributeValueView(GenericAPIView):
    permission_classes = []

    def get(self, request, attributes_value_id):
        attribute_value = DeviceConfigurationFieldValue.objects.get(id=attributes_value_id)
        serializer = AttributeValueSerializer(attribute_value)
        return Response(serializer.data)

    def post(self, request, attributes_value_id):
        attribute_value = DeviceConfigurationFieldValue.objects.get(id=attributes_value_id)
        # self.check_object_permissions(request, review)
        serializer = AttributeValueSerializer(attribute_value, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, attributes_value_id):
        attribute_value = DeviceConfigurationFieldValue.objects.get(id=attributes_value_id)
        # self.check_object_permissions(request, review)
        attribute_value.delete()
        return Response("OK")


class GetListOfAttributeValuesView(APIView):
    permission_classes = [
        # IsAuthenticated,
    ]

    def get(self, request, device_id):
        attribute_values = DeviceConfigurationFieldValue.objects.filter(device=device_id)
        serializer = AttributeValueSerializer(attribute_values, many=True)
        return Response(serializer.data)