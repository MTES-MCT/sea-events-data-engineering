from abc import ABC, abstractmethod
from typing import Collection

from src.entities import Ship


class ShipClientABC(ABC):
    @abstractmethod
    def get_ships_by_registry_number(self, registry_numbers: Collection[str]) -> list[Ship]:
        pass
