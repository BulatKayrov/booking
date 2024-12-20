from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from core.api.v1.serializers.room_serializer import ResponseRoomSerializer, RoomInSerializer, RoomUpdateSerializer
from core.domain.dto.room import RoomInDTO, RoomOutDTO
from core.domain.repositories.room import RoomRepository
from core.domain.services.room_service import RoomService

_room_service = RoomService(repository=RoomRepository())


@api_view(['GET'])
def get_rooms(request: Request, pk: int = None):
    """получение списка номеров для конкретного отеля или получения всех номеров"""
    if pk is None:
        obj = _room_service.get_list_rooms(hotel_pk=pk)
    else:
        obj = _room_service.get_list_rooms(hotel_pk=pk)
    return Response({'data': ResponseRoomSerializer(obj, many=True).data})


@api_view(['POST'])
def create_record_room(request: Request):
    """добавление нового номера (только для администраторов)"""
    sr = RoomInSerializer(data=request.data)
    if sr.is_valid(raise_exception=True):
        obj = _room_service.create_room(data=RoomInDTO(**sr.validated_data))
        return Response({'status': 201, 'object': ResponseRoomSerializer(instance=obj).data})


@api_view(['PUT'])
def update_record_room(request: Request, pk: int):
    """обновление информации о номере (только для администраторов)"""
    sr = RoomUpdateSerializer(data=request.data)
    if sr.is_valid(raise_exception=True):
        obj = _room_service.update_room(pk=pk, data=RoomInDTO(**sr.validated_data))
        return Response({'status': 201, 'object': ResponseRoomSerializer(instance=obj).data})


@api_view(['DELETE'])
def delete_room(request: Request, pk: int):
    """даление номера (только для администраторов)"""
    _room_service.delete_room(pk=pk)
    return Response({'status': 200})


@api_view(['GET'])
def detail_room(request: Request, pk: int):
    return Response({'object': ResponseRoomSerializer(instance=_room_service.get_room(pk=pk)).data})