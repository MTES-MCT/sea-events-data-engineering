from typing import Collection

from src.entities import AccidentEnim, Ship, AccidentEnimWithShipData
from src.repositories import (
    ShipClient,
    EnimAccidentClient,
    EnimAccidentClientWithShipsData,
    ShipClientABC,
    EnimAccidentClientABC,
    EnimAccidentClientWithShipsDataABC,
)

ship_client: ShipClientABC = ShipClient()
enim_accident_client: EnimAccidentClientABC = EnimAccidentClient()
enim_accident_with_ships_data_client: EnimAccidentClientWithShipsDataABC = EnimAccidentClientWithShipsData()


def push_enim_accidents_with_ships_data_to_storage(enim_accidents_with_ship_data: list[AccidentEnimWithShipData]) -> None:
    for enim_accident_with_ship_data in enim_accidents_with_ship_data:
        enim_accident_with_ships_data_client.create(enim_accident_with_ship_data)


def get_new_enim_accidents() -> list[AccidentEnim]:
    return enim_accident_client.get_all()


def get_ships(registry_numbers: Collection[str]) -> list[Ship]:
    return ship_client.get_ships_by_registry_number(registry_numbers)
