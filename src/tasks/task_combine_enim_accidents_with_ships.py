from typing import Collection

from prefect import Task

from src.entities import AccidentEnim, Ship, AccidentEnimWithShipData


class CombineAccidentWithShip(Task):
    
    def run(self, ship_data: Collection[Ship], enim_accidents: Collection[AccidentEnim]) -> list[AccidentEnimWithShipData]:
        combined_data = []
        for enim_accident in enim_accidents:
            ship = self._find_ship(enim_accident, ship_data)

            combined_attributes = {
                'ship_name': None,
                'num_version': None,
                'IMO_number': None,
                'flag_state': None,
                'gross_tonnage': None,
                'built_year': None,
                'hull_material': None,
                'propulsion_type': None,
                'length_overall': None,
                'national_location': None,
                'navigation_type_navpro': None,
                'navigation_type_gina': None,
                'ship_type': None
            }
            if ship:
                combined_attributes = ship.dict()
                combined_attributes.pop('registry_number')

            combined_data.append(
                AccidentEnimWithShipData(
                    **enim_accident.dict(),
                    **combined_attributes,
                )
            )
        return combined_data

    def _find_ship(self, enim_accident: AccidentEnim, ship_data: Ship) -> Ship | None:
        primary_key_name = 'registry_number'
        expected_primary_key = getattr(enim_accident, primary_key_name)
        for ship in ship_data:
            actual_primary_key = getattr(ship, primary_key_name)
            if actual_primary_key == expected_primary_key:
                return ship
        else:
            return None

combine_enim_accidents_with_ships = CombineAccidentWithShip()
