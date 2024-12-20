from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RoomInDTO:
    type_room: Optional[int] = None
    price: Optional[int] = None
    is_free: Optional[int] = None
    hotel_id: Optional[int] = None

    def to_dict(self):
        return {
            'type_room': self.type_room,
            'price': self.price,
            'is_free': self.is_free,
            'hotel_id': self.hotel_id,
        }


@dataclass
class RoomOutDTO(RoomInDTO):
    pk: Optional[int] = None
