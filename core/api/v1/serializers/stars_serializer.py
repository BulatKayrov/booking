from rest_framework import serializers


class StarSerializer(serializers.Serializer):
    value = serializers.IntegerField()
