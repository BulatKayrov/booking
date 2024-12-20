from core.apps.model.room import Room
from core.domain.dto.room import RoomInDTO, RoomOutDTO
from core.domain.interfaces.iroom import IRoomRepository


class RoomRepository(IRoomRepository):
    model = Room

    def get_list_room(self, hotel_pk: int = None):
        if hotel_pk:
            return list(self.model.objects.filter(hotel__pk=hotel_pk))
        return list(self.model.objects.all())

    def create_room(self, data: RoomInDTO):
        obj = self.model.objects.create(**data.to_dict())
        return obj

    def delete_room(self, pk: int) -> None:
        obj = self.model.objects.get(pk=pk)
        obj.delete()
        return None

    def update_room(self, pk: int, data: RoomInDTO):
        obj = self.model.objects.get(pk=pk)
        for key, value in data.to_dict().items():
            if value is not None:
                setattr(obj, key, value)

        obj.save()
        return obj

    def get_room(self, pk: int):
        obj = self.model.objects.get(pk=pk)
        return obj
