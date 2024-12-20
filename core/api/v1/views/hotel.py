from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core.api.v1.serializers.hotel_serializers import (
    ResponseHotelSerializer,
    CreateHotelSerializer,
    HotelFullInfoSerializer, UpdateHotelSerializer
)
from core.domain.dto.hotel import HotelInDTO
from core.domain.repositories.hotel import HotelRepository
from core.domain.services.hotel_service import HotelService

_hotel_service = HotelService(repository=HotelRepository())


@api_view(['GET'])
def all_hotels(request: Request):
    """получение списка отелей"""
    list_result = _hotel_service.get_list_hotels()
    sr = ResponseHotelSerializer(instance=list_result, many=True)
    return Response({'result': sr.data})


@api_view(['GET'])
def get_hotels(request: Request, pk: int):
    """получение информации об отеле"""
    obj = _hotel_service.get_hotel(pk=pk)
    sr = HotelFullInfoSerializer(instance=obj)
    return Response({'result': sr.data})


@api_view(['POST'])
def create_new_hotel(request: Request):
    """добавление нового отеля (только для администраторов)"""
    sr = CreateHotelSerializer(data=request.data)
    if sr.is_valid(raise_exception=True):
        obj = _hotel_service.create_record(data=HotelInDTO(**sr.validated_data))
        return Response({'status': 201, 'new_object': ResponseHotelSerializer(instance=obj).data})


@api_view(['PUT'])
def put_hotel(request: Request, pk: int):
    """обновление информации об отеле (только для администраторов)"""
    sr = UpdateHotelSerializer(data=request.data)
    if sr.is_valid(raise_exception=True):
        obj = _hotel_service.put_hotel(pk=pk, data=HotelInDTO(**sr.validated_data))
        return Response({'status': 200, 'updated object': ResponseHotelSerializer(instance=obj).data})


@api_view(['DELETE'])
def delete_hotel(request: Request, pk: int):
    """удаление отеля (только для администраторов)"""
    _hotel_service.delete_item(pk=pk)
    return Response({'status': 200})
