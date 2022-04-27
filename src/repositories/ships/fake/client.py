from typing import Collection
import shelve

from .database import SHELVE_NAME
from src.repositories.ships.abc import ShipClientABC
from src.entities import Ship


class ShipClientFake(ShipClientABC):
    def get_by_registry_number(self, registry_numbers: Collection[str]) -> list[Ship]:
        with shelve.open(SHELVE_NAME) as opened_shelf:
            ships = []
            for registry_number in set(registry_numbers):
                if str(registry_number) in opened_shelf:
                    ships.append(Ship(**opened_shelf[str(registry_number)]))
            return ships
