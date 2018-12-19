from django.urls import path, include

app_name = 'inventory'

urlpatterns = [
    path('customers/', include('inventory.customers.urls')),
    path('devices/', include('inventory.devices.urls')),
    path('device_models/', include('inventory.device_models.urls')),
    path('lorawans/', include('inventory.lorawan.urls')),
    path('configuration_fields/', include('inventory.configuration_fields.urls')),
    path('attributes_values/', include('inventory.attributes_values.urls')),
]