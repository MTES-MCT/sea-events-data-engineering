import shelve

from .database import SHELVE_NAME
from src.repositories.enim_accidents_with_ships_data.abc import EnimAccidentClientWithShipsDataABC
from src.entities import AccidentEnimWithShipData

class EnimAccidentClientWithShipsDataFake(EnimAccidentClientWithShipsDataABC):

    def create(self, data_to_load: AccidentEnimWithShipData) -> None:
        with shelve.open(SHELVE_NAME) as db:
            identifier = data_to_load.registry_number
            if identifier in db:
                raise ValueError(f'Accident with registry number {identifier} already exists')

            db[str(identifier)] = data_to_load.dict()
