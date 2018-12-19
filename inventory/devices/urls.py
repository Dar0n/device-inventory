from django.urls import path

from inventory.devices.views import PostNewDevice, GetListOfDevicesView, GetUpdateDeleteDeviceView, GetListOfDevicesForModelView

app_name = 'devices'

urlpatterns = [
    path('newdevice/<int:device_model_id>/', PostNewDevice.as_view(), name='new-device'),
    path('device/<int:device_id>/', GetUpdateDeleteDeviceView.as_view(), name='get-update-delete-devices'),
    path('listdevices/', GetListOfDevicesView.as_view(), name='get-list-of-devices'),
    path('listdevicesformodel/<int:device_model_id>/', GetListOfDevicesForModelView.as_view(), name='get-list-of-devices-for-model'),
]
