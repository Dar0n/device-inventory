from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory.customers.serializers import CustomerSerializer
from inventory.models import Customer


class PostNewCustomer(APIView):
    permission_classes = []

    def post(self, request, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer = serializer.create(serializer.validated_data)
        return Response(CustomerSerializer(customer).data)


class GetUpdateDeleteCustomerView(GenericAPIView):
    permission_classes = []

    def get(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def post(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        # self.check_object_permissions(request, review)
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, customer_id):
        customer = Customer.objects.get(id=customer_id)
        # self.check_object_permissions(request, review)
        customer.delete()
        return Response("OK")


class GetListOfCustomersView(APIView):
    permission_classes = [
        # IsAuthenticated,
    ]

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)