from django.urls import path

from inventory.device_models.views import PostNewDeviceModel, GetUpdateDeleteDeviceModelView, GetListOfAllDeviceModelsView

app_name = 'device_models'

urlpatterns = [
    path('newdevicemodel/', PostNewDeviceModel.as_view(), name='new-device-model'),
    path('device_model/<int:device_model_id>/', GetUpdateDeleteDeviceModelView.as_view(), name='get-update-delete-device-model'),
    path('listmodels/all/', GetListOfAllDeviceModelsView.as_view(), name='get-list-of-all-device-models'),
]
