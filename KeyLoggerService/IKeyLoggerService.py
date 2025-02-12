from abc import ABC, abstractmethod

class IKeloggerService(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get(self):
        pass