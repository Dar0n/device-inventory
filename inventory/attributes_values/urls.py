from django.urls import path

from inventory.attributes_values.views import PostNewAttributeValue, GetUpdateDeleteAttributeValueView, GetListOfAttributeValuesView

app_name = 'attributes_values'

urlpatterns = [
    path('newattributevalue/<int:device_id>/<int:configuration_field_id>/', PostNewAttributeValue.as_view(), name='new-attribute-value'),
    path('attributesvalue/<int:attributes_value_id>/', GetUpdateDeleteAttributeValueView.as_view(), name='get-update-delete-attribute-value'),
    path('listattributevalues/<int:device_id>/', GetListOfAttributeValuesView.as_view(), name='get-list-of-attribute-values'),
]
