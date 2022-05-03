from typing import Collection

from prefect import Task

from src.entities import AccidentEnim, Ship
from src.repositories import ShipClient


class ExtractShipData(Task):

    _ship_client = ShipClient()

    def run(self, enim_accidents: Collection[AccidentEnim]) -> list[Ship]:  # type: ignore
        registry_numbers = [str(accident.registry_number) for accident in enim_accidents]
        return self._ship_client.get_by_registry_number(registry_numbers)


extract_ships_data = ExtractShipData()
