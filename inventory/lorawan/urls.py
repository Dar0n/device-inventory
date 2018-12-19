from django.urls import path

from inventory.lorawan.views import PostNewLoRaWAN, GetUpdateDeleteLorawanView, GetListOfLorawansView

app_name = 'lorawans'

urlpatterns = [
    path('newlorawan/', PostNewLoRaWAN.as_view(), name='new-lorawan'),
    path('lorawan/<int:lorawan_id>/', GetUpdateDeleteLorawanView.as_view(), name='get-update-delete-lorawans'),
    path('listlorawans/', GetListOfLorawansView.as_view(), name='get-list-of-lorawans'),
]
