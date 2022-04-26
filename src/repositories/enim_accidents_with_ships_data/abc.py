from abc import ABC, abstractmethod

from src.entities import AccidentEnimWithShipData


class EnimAccidentClientWithShipsDataABC(ABC):
    @abstractmethod
    def create(self, data_to_load: AccidentEnimWithShipData) -> None:
        pass
