from prefect import Task

from src.connectors import push_enim_accidents_with_ships_data_to_storage
from src.entities import AccidentEnimWithShipData

class LoadEnimAccidentWithShip(Task):
    
    def run(self, enim_accidents_with_ship_data: AccidentEnimWithShipData) -> None:
        push_enim_accidents_with_ships_data_to_storage(enim_accidents_with_ship_data)

load_enim_accidents_with_ship = LoadEnimAccidentWithShip()
