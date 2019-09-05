from django.urls import path
from .views import doner_list,new_doner
app_name = 'bloodDonation'
urlpatterns = [
    path('', doner_list, name='list'),
    path('new/', new_doner, name='newDoner'),
]