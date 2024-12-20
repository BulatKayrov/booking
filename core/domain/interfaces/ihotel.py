import dataclasses
from abc import ABC, abstractmethod


class IHotelRepository(ABC):

    @abstractmethod
    def get_list_hotel(self):
        ...

    @abstractmethod
    def create_hotel(self, data):
        ...

    @abstractmethod
    def get_hotel(self, pk: int):
        ...

    @abstractmethod
    def put_hotel(self, pk: int, data: dataclasses.dataclass):
        ...

    @abstractmethod
    def delete_hotel(self, pk: int):
        ...