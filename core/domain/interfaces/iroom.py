from abc import ABC, abstractmethod

from core.domain.dto.room import RoomInDTO, RoomOutDTO


class IRoomRepository(ABC):

    @abstractmethod
    def get_list_room(self, hotel_pk: int = None):
        ...

    @abstractmethod
    def create_room(self, data: RoomInDTO):
        ...

    @abstractmethod
    def delete_room(self, pk: int):
        ...

    @abstractmethod
    def update_room(self, pk: int, data: RoomOutDTO):
        ...

    @abstractmethod
    def get_room(self, pk: int):
        ...