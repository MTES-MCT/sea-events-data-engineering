from typing import Collection

from config import Config
from .abc import ShipClientABC
from src.entities import Ship


class ShipClient(ShipClientABC):
    def __init__(self, ship_repository: str = Config.SHIP_CLIENT):
        self._implementation: ShipClientABC = NotImplemented
        match ship_repository:
            case "dam_oracle":
                from src.repositories.ships.dam_oracle.client import ShipClientDamOracle

                self._implementation = ShipClientDamOracle()
            case "fake":
                from src.repositories.ships.fake.client import ShipClientFake

                self._implementation = ShipClientFake()
            case _:
                raise ValueError(f"Unknown ship client: {Config.SHIP_CLIENT}")

    def get_by_registry_number(self, registry_numbers: Collection[str]) -> list[Ship]:
        return self._implementation.get_by_registry_number(registry_numbers)
