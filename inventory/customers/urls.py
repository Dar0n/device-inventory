from django.urls import path

from inventory.customers.views import PostNewCustomer, GetUpdateDeleteCustomerView, GetListOfCustomersView
from . import views

app_name = 'customers'

urlpatterns = [
    path('newcustomer/', PostNewCustomer.as_view(), name='new-customer'),
    path('customer/<int:customer_id>/', GetUpdateDeleteCustomerView.as_view(), name='get-update-delete-customers'),
    path('listcustomers/', GetListOfCustomersView.as_view(), name='get-list-of-customers'),
]
