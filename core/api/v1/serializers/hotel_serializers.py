from rest_framework import serializers

from core.api.v1.serializers.room_serializer import ResponseRoomSerializer
from core.api.v1.serializers.stars_serializer import StarSerializer


class ResponseHotelSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=500)


class CreateHotelSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=500)
    description = serializers.CharField(max_length=500)


class HotelFullInfoSerializer(ResponseHotelSerializer):
    rooms = ResponseRoomSerializer(many=True)
    stars = StarSerializer(many=True)


class UpdateHotelSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    address = serializers.CharField(max_length=500, required=False)
    description = serializers.CharField(max_length=500, required=False)