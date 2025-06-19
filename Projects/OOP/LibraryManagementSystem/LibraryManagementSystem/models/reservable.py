from abc import ABC, abstractmethod

class Reservable(ABC):
    @abstractmethod
    def reserve(self, user):
        pass