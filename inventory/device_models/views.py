from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.device_models.serializers import DeviceModelSerializer
from inventory.models import DeviceModel


class PostNewDeviceModel(APIView):
    permission_classes = []

    def post(self, request):
        serializer = DeviceModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device_model = serializer.create(serializer.validated_data)
        return Response(DeviceModelSerializer(device_model).data)


class GetUpdateDeleteDeviceModelView(GenericAPIView):
    permission_classes = []

    def get(self, request, device_model_id):
        device_model = DeviceModel.objects.get(id=device_model_id)
        serializer = DeviceModelSerializer(device_model)
        return Response(serializer.data)

    def post(self, request, device_model_id):
        device_model = DeviceModel.objects.get(id=device_model_id)
        # self.check_object_permissions(request, review)
        serializer = DeviceModelSerializer(device_model, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, device_model_id):
        device_model = DeviceModel.objects.get(id=device_model_id)
        # self.check_object_permissions(request, review)
        device_model.delete()
        return Response("OK")


class GetListOfAllDeviceModelsView(APIView):
    permission_classes = [
        # IsAuthenticated,
    ]

    def get(self, request):
        device_models = DeviceModel.objects.all()
        serializer = DeviceModelSerializer(device_models, many=True)
        return Response(serializer.data)
