from typing import Collection

from prefect import Task

from src.entities import AccidentEnim, Ship
from src.connectors import get_ships


class ExtractShipData(Task):
    
    def run(self, enim_accidents: Collection[AccidentEnim]) -> Ship:
        registry_numbers = [accident.registry_number for accident in enim_accidents]
        return get_ships(registry_numbers)

extract_ships_data = ExtractShipData()
