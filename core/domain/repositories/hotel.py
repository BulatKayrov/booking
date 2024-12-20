from core.apps.model.hotel import Hotel
from core.domain.dto.hotel import HotelInDTO, HotelOutDTO, HotelFullInfoDTO
from core.domain.dto.room import RoomOutDTO
from core.domain.dto.star import StarDTO
from core.domain.interfaces.ihotel import IHotelRepository


class HotelRepository(IHotelRepository):
    model = Hotel

    def get_list_hotel(self):
        return list(self.model.objects.all())

    def create_hotel(self, data: HotelInDTO):
        obj = self.model.objects.create(
            title=data.title, description=data.description, address=data.address
        )
        return HotelOutDTO(pk=obj.pk, title=obj.title, description=obj.description, address=obj.address)

    def get_hotel(self, pk: int) -> HotelFullInfoDTO:
        obj = self.model.objects.get(pk=pk)  # Hotel
        return HotelFullInfoDTO(
            pk=obj.pk,
            title=obj.title,
            address=obj.address,
            description=obj.description,
            rooms=[
                RoomOutDTO(
                    pk=item.pk,
                    type_room=item.type_room,
                    price=item.price,
                    is_free=item.is_free,
                    hotel_id=obj.pk
                )
                for item in obj.rooms.all()
            ],
            stars=[
                StarDTO(
                    value=item.value
                )
                for item in obj.stars.all()
            ]
        )

    def put_hotel(self, pk: int, data: HotelInDTO):
        obj = self.model.objects.get(pk=pk)

        for key, value in data.to_dict().items():
            if value is not None:
                setattr(obj, key, value)

        obj.save()
        return HotelOutDTO(
            pk=obj.pk,
            title=obj.title,
            address=obj.address,
            description=obj.description
        )

    def delete_hotel(self, pk: int):
        self.model.objects.get(pk=pk).delete()
        return None