from django.urls import path

from .views.hotel import all_hotels, create_new_hotel, get_hotels, put_hotel, delete_hotel
from .views.room import get_rooms, create_record_room, update_record_room, delete_room, detail_room

app_name = 'v1'

urlpatterns = [

    path('hotels/', all_hotels),
    path('hotels/update/<int:pk>', put_hotel),
    path('hotels/<int:pk>', get_hotels),
    path('create/hotels/', create_new_hotel),
    path('delete/hotels/<int:pk>', delete_hotel),

    path('rooms/', get_rooms),
    path('create/', create_record_room),
    path('rooms/<int:pk>', get_rooms),
    path('delete/<int:pk>', delete_room),
    path('update/<int:pk>', update_record_room),
    path('detail/<int:pk>', detail_room),

]