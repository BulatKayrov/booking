from abc import ABC, abstractmethod


class IBookingRepository(ABC):

    @abstractmethod
    def get_full_info(self):
        ...

    @abstractmethod
    def create_booking(self):
        ...

    @abstractmethod
    def put_booking(self):
        ...


    @abstractmethod
    def delete_booking(self):
        ...