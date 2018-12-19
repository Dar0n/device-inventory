from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.configuration_fields.serializers import ConfigurationFieldSerializer
from inventory.models import ConfigurationField


class PostNewConfigurationField(APIView):
    permission_classes = []

    def post(self, request, device_model_id):
        serializer = ConfigurationFieldSerializer(data=request.data,
                                                  context={
                                                      "device_model_id": device_model_id,
                                                  }
                                                  )
        serializer.is_valid(raise_exception=True)
        configuration_field = serializer.create(serializer.validated_data)
        return Response(ConfigurationFieldSerializer(configuration_field).data)


class GetUpdateDeleteConfigurationFieldView(GenericAPIView):
    permission_classes = []

    def get(self, request, configuration_field_id):
        configuration_field = ConfigurationField.objects.get(id=configuration_field_id)
        serializer = ConfigurationFieldSerializer(configuration_field)
        return Response(serializer.data)

    def post(self, request, configuration_field_id):
        configuration_field = ConfigurationField.objects.get(id=configuration_field_id)
        # self.check_object_permissions(request, review)
        serializer = ConfigurationFieldSerializer(configuration_field, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, configuration_field_id):
        configuration_field = ConfigurationField.objects.get(id=configuration_field_id)
        # self.check_object_permissions(request, review)
        configuration_field.delete()
        return Response("OK")


class GetListOfConfigurationFieldsView(APIView):
    permission_classes = [
        # IsAuthenticated,
    ]

    def get(self, request, device_model_id):
        configuration_fields = ConfigurationField.objects.filter(device_model=device_model_id)
        serializer = ConfigurationFieldSerializer(configuration_fields, many=True)
        return Response(serializer.data)