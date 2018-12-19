from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.devices.serializers import DeviceSerializer
from inventory.models import Device


class PostNewDevice(APIView):
    permission_classes = []

    def post(self, request, device_model_id):
        serializer = DeviceSerializer(data=request.data, context={
            "device_model_id": device_model_id,
        })
        serializer.is_valid(raise_exception=True)
        device = serializer.create(serializer.validated_data)
        return Response(DeviceSerializer(device).data)


class GetUpdateDeleteDeviceView(GenericAPIView):
    permission_classes = []

    def get(self, request, device_id):
        device = Device.objects.get(id=device_id)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def post(self, request, device_id):
        device = Device.objects.get(id=device_id)
        # self.check_object_permissions(request, review)
        serializer = DeviceSerializer(device, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, device_id):
        device = Device.objects.get(id=device_id)
        # self.check_object_permissions(request, review)
        device.delete()
        return Response("OK")

class GetListOfDevicesView(APIView):
    permission_classes = [
        # IsAuthenticated,
    ]

    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)


class GetListOfDevicesForModelView(APIView):
    permission_classes = []

    def get(self, request, device_model_id):
        devices = Device.objects.filter(device_model=device_model_id)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)