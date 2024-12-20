from typing import List

from core.domain.dto.room import RoomInDTO, RoomOutDTO
from core.domain.interfaces.iroom import IRoomRepository


class RoomService:

    def __init__(self, repository: IRoomRepository):
        self.__repository: IRoomRepository = repository

    def get_list_rooms(self, hotel_pk: int = None) -> List[RoomOutDTO]:
        return [
            RoomOutDTO(
                pk=obj.pk,
                type_room=obj.type_room,
                price=obj.price,
                is_free=obj.is_free,
                hotel_id=obj.hotel.pk,
            )
            for obj in self.__repository.get_list_room(hotel_pk=hotel_pk)
        ]

    def create_room(self, data: RoomInDTO) -> RoomOutDTO:
        obj = self.__repository.create_room(data=data)
        return RoomOutDTO(
            pk=obj.pk,
            type_room=obj.type_room,
            price=obj.price,
            is_free=obj.is_free,
            hotel_id=obj.hotel.pk,
        )

    def update_room(self, pk: int, data: RoomInDTO) -> RoomOutDTO:
        obj = self.__repository.update_room(pk=pk, data=data)
        return RoomOutDTO(
            type_room=obj.type_room, price=obj.price, is_free=obj.is_free, hotel_id=obj.hotel.pk, pk=obj.pk
        )

    def delete_room(self, pk: int) -> None:
        return self.__repository.delete_room(pk=pk)

    def get_room(self, pk: int):
        obj = self.__repository.get_room(pk=pk)
        return RoomOutDTO(
            pk=obj.pk,
            type_room=obj.type_room,
            price=obj.price,
            is_free=obj.is_free,
            hotel_id=obj.hotel.pk,
        )
