from django.urls import path

from inventory.configuration_fields.views import PostNewConfigurationField, GetUpdateDeleteConfigurationFieldView, GetListOfConfigurationFieldsView

app_name = 'configuration_fields'

urlpatterns = [
    path('newconfigurationfield/<int:device_model_id>/', PostNewConfigurationField.as_view(), name='new-configuration-field'),
    path('configurationfield/<int:configuration_field_id>/', GetUpdateDeleteConfigurationFieldView.as_view(), name='get-update-delete-configuration-field'),
    path('listconfigurationfields/<int:device_model_id>/', GetListOfConfigurationFieldsView.as_view(), name='get-list-of-configuration-fields'),
]
