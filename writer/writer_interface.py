from abc import ABC, abstractmethod


class IWriter(ABC):
    @abstractmethod
    def write(self, data: str, target_id: str) -> bool:
        """
        Write data to a destination.

        Parameters:
        data (str): The data to be written.
        target_id (str): The id of the targeted machine the write operation.
        """
        pass


    