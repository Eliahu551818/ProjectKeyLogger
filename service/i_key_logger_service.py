from abc import ABC, abstractmethod

# An Interface To KeyLoggerService
class IKeloggerService(ABC):

    # Start Method starts the service
    @abstractmethod
    def start(self):
        pass

    # Stop Method stops the service
    @abstractmethod
    def stop(self):
        pass

    # Get Method Returns the data that stored
    @abstractmethod
    def get(self):
        pass