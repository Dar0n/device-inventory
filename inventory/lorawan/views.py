from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.lorawan.serializers import LoRaWANSerializer
from inventory.models import LoRaWAN


class PostNewLoRaWAN(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = LoRaWANSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lorawan = serializer.create(serializer.validated_data)
        return Response(LoRaWANSerializer(lorawan).data)


class GetUpdateDeleteLorawanView(GenericAPIView):
    permission_classes = []

    def get(self, request, lorawan_id):
        lorawan = LoRaWAN.objects.get(id=lorawan_id)
        serializer = LoRaWANSerializer(lorawan)
        return Response(serializer.data)

    def post(self, request, lorawan_id):
        lorawan = LoRaWAN.objects.get(id=lorawan_id)
        # self.check_object_permissions(request, review)
        serializer = LoRaWANSerializer(lorawan, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, lorawan_id):
        lorawan = LoRaWAN.objects.get(id=lorawan_id)
        # self.check_object_permissions(request, review)
        lorawan.delete()
        return Response("OK")


class GetListOfLorawansView(APIView):
    permission_classes = [
        # IsAuthenticated,
    ]

    def get(self, request):
        lorawans = LoRaWAN.objects.all()
        serializer = LoRaWANSerializer(lorawans, many=True)
        return Response(serializer.data)