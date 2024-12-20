from rest_framework import serializers


class RoomInSerializer(serializers.Serializer):
    type_room = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    is_free = serializers.CharField()
    hotel_id = serializers.IntegerField()

class ResponseRoomSerializer(RoomInSerializer):
    pk = serializers.IntegerField()


class RoomUpdateSerializer(serializers.Serializer):
    type_room = serializers.IntegerField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    is_free = serializers.CharField(required=False)
    hotel_id = serializers.IntegerField(required=False)


