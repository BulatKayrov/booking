from django.contrib import admin
from django.contrib.auth import get_user_model

from .hotel import Hotel
from .star import Start
from .room import Room
from .booking import Booking


User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hotel)
admin.site.register(Start)
admin.site.register(Room)
admin.site.register(Booking)