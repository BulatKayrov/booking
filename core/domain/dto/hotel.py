from dataclasses import dataclass
from typing import List

from core.domain.dto.room import RoomOutDTO
from core.domain.dto.star import StarDTO


@dataclass
class HotelInDTO:
    title: str
    address: str
    description: str

    def to_dict(self):
        return {
            'title': self.title,
            'address': self.address,
            'description': self.description
        }


@dataclass
class HotelOutDTO(HotelInDTO):
    pk: int


@dataclass
class HotelFullInfoDTO(HotelOutDTO):
    rooms: List[RoomOutDTO]
    stars: List[StarDTO]
