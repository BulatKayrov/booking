from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class BookingInDTO:
    user_id: Optional[int] = None
    room_id: Optional[List[int]] = None
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    status: Optional[str] = None

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'room_id': self.room_id,
            'check_in': self.check_in,
            'check_out': self.check_out,
            'status': self.status,
        }


@dataclass
class BookingOutDTO(BookingInDTO):
    pk: Optional[int] = None
