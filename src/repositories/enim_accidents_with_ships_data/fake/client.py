import shelve

from .database import SHELVE_NAME
from src.repositories.enim_accidents_with_ships_data.abc import (
    EnimAccidentWithShipsDataClientABC,
)
from src.entities import AccidentEnimWithShipData


class EnimAccidentClientWithShipsDataFake(EnimAccidentWithShipsDataClientABC):
    def create_many(self, data_to_load: list[AccidentEnimWithShipData]) -> None:
        with shelve.open(SHELVE_NAME) as opened_shelf:
            for data in data_to_load:
                self._create_one(opened_shelf, data)

    def _create_one(
        self, opened_shelf: shelve.Shelf, data_to_load: AccidentEnimWithShipData
    ) -> None:
        identifier = data_to_load.registry_number
        if identifier in opened_shelf:
            raise ValueError(
                f"Accident with registry number {identifier} already exists"
            )

        opened_shelf[str(identifier)] = data_to_load.dict()
