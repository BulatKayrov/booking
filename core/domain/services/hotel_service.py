from typing import List

from core.domain.dto.hotel import HotelInDTO, HotelOutDTO
from core.domain.interfaces.ihotel import IHotelRepository


class HotelService:
    def __init__(self, repository: IHotelRepository):
        self.__repository: IHotelRepository = repository

    def get_list_hotels(self) -> List[HotelOutDTO]:
        return [
            HotelOutDTO(pk=obj.pk, title=obj.title, address=obj.address, description=obj.description)
            for obj in self.__repository.get_list_hotel()
        ]

    def create_record(self, data: HotelInDTO):
        return self.__repository.create_hotel(data=data)

    def get_hotel(self, pk: int):
        return self.__repository.get_hotel(pk=pk)

    def put_hotel(self, pk: int, data: HotelInDTO) -> HotelOutDTO:
        return self.__repository.put_hotel(pk=pk, data=data)

    def delete_item(self, pk: int):
        return self.__repository.delete_hotel(pk=pk)
