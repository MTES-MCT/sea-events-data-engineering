from config import Config
from .abc import EnimAccidentWithShipsDataClientABC
from src.entities import AccidentEnimWithShipData


class EnimAccidentWithShipsDataClient(EnimAccidentWithShipsDataClientABC):
    def __init__(
        self,
        enim_accidents_with_ships_data_repository: str = Config.ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT,
    ):
        self._implementation: EnimAccidentWithShipsDataClientABC = NotImplemented
        match enim_accidents_with_ships_data_repository:
            case "fake":
                from src.repositories.enim_accidents_with_ships_data.fake.client import (
                    EnimAccidentClientWithShipsDataFake,
                )

                self._implementation = EnimAccidentClientWithShipsDataFake()
            case "sqlite":
                from src.repositories.enim_accidents_with_ships_data.sqlite.client import (
                    EnimAccidentClientWithShipsDataSQLite,
                )

                self._implementation = EnimAccidentClientWithShipsDataSQLite()
            case _:
                raise ValueError(
                    f"Unknown enim accident with ships data client: {Config.ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT}"
                )

    def create_many(self, data_to_load: list[AccidentEnimWithShipData]) -> None:
        self._implementation.create_many(data_to_load)
