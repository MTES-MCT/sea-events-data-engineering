from typing import Collection

from prefect import Task

from src.entities import AccidentEnim, Ship, AccidentEnimWithShipData


# static type checking limitation: https://github.com/PrefectHQ/prefect/issues/4649
class CombineAccidentWithShip(Task):
    def run(  # type: ignore
        self, available_ships: Collection[Ship], enim_accidents: Collection[AccidentEnim]
    ) -> list[AccidentEnimWithShipData]:
        combined_data = []
        for enim_accident in enim_accidents:
            ship = self._find_ship(enim_accident, available_ships)
            enim_accident_with_ship_data = self._add_ship_data_to_enim_accident(enim_accident, ship)
            combined_data.append(enim_accident_with_ship_data)

        return combined_data

    def _add_ship_data_to_enim_accident(self, enim_accident: AccidentEnim, ship: Ship | None) -> AccidentEnimWithShipData:

            combined_attributes = {
                "ship_name": None,
                "num_version": None,
                "IMO_number": None,
                "flag_state": None,
                "gross_tonnage": None,
                "built_year": None,
                "hull_material": None,
                "propulsion_type": None,
                "length_overall": None,
                "national_location": None,
                "navigation_type_navpro": None,
                "navigation_type_gina": None,
                "ship_type": None,
            }
            if ship:
                combined_attributes = ship.dict()
                combined_attributes.pop("registry_number")

            return AccidentEnimWithShipData(
                **enim_accident.dict(),
                **combined_attributes,
            )

    def _find_ship(self, enim_accident: AccidentEnim, ship_data: Collection[Ship]) -> Ship | None:
        primary_key_name = "registry_number"
        expected_primary_key = getattr(enim_accident, primary_key_name)
        for ship in ship_data:
            actual_primary_key = getattr(ship, primary_key_name)
            if actual_primary_key == expected_primary_key:
                return ship
        else:
            return None


combine_enim_accidents_with_ships = CombineAccidentWithShip()
