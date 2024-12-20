from abc import ABC, abstractmethod


class IStarRepository(ABC):

    @abstractmethod
    def create_record(self):
        pass