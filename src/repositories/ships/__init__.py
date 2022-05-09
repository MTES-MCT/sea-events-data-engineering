from typing import Collection

from config import Config
from .abc import ShipClientABC
from src.entities import Ship


def repository_setup(repository_implementation: str):
    """
    Initialize the database and restore initial data and state.
    """
    match repository_implementation:
        case "fake":
            from .fake.database import repository_setup as fake_repository_setup

            fake_repository_setup()
        case "dam_oracle":
            from .dam_oracle.database import (
                repository_setup as dam_oracle_repository_setup,
            )

            dam_oracle_repository_setup()
        case _:
            raise ValueError(
                f"Unknown repository_implementation: {repository_implementation}"
            )


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
