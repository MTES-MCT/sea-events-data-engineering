from abc import ABC, abstractmethod

from src.entities import AccidentEnimWithShipData


class EnimAccidentWithShipsDataClientABC(ABC):
    @abstractmethod
    def create_many(self, data_to_load: list[AccidentEnimWithShipData]) -> None:
        pass
