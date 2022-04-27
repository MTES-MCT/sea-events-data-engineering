from prefect import Task

from src.entities import AccidentEnimWithShipData
from src.repositories import EnimAccidentWithShipsDataClient


class LoadEnimAccidentWithShip(Task):
    _enim_accident_with_ship_data_client = EnimAccidentWithShipsDataClient()

    def run(self, enim_accidents_with_ship_data: AccidentEnimWithShipData) -> None:
        self._enim_accident_with_ship_data_client.create_many(
            enim_accidents_with_ship_data
        )


load_enim_accidents_with_ship = LoadEnimAccidentWithShip()
