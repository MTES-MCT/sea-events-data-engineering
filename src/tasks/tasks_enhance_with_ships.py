from typing import Collection

from prefect import Task

from src.entities import (
    AccidentEnim,
    Ship,
    AccidentEnimWithShipData,
    SeamisReport,
    SeamisReportWithShipData,
)


class CombineSeamisReportsWithShips(Task):
    def run(  # type: ignore
        self,
        available_ships: Collection[Ship],
        seamis_reports: Collection[SeamisReport],
    ) -> Collection[SeamisReportWithShipData]:
        self.logger.info("Combining seamis reports with ships")
        self.logger.info(f"Seamis reports: {seamis_reports}")
        self.logger.info(f"Available ships: {available_ships}")
        enhanced_seamis_reports = []
        for seamis_report in seamis_reports:
            ship = self._find_ship(seamis_report, available_ships)
            enhanced_seamis_report = self._enhance_seamis_report_with_ship_data(
                seamis_report, ship
            )
            enhanced_seamis_reports.append(enhanced_seamis_report)
        self.logger.info(f"Enhanced seamis reports: {enhanced_seamis_reports}")
        return enhanced_seamis_reports

    def _find_ship(
        self, seamis_report: SeamisReport, ship_data: Collection[Ship]
    ) -> Ship | None:
        primary_key_name = "registry_number"
        expected_primary_key = getattr(seamis_report, primary_key_name)
        for ship in ship_data:
            actual_primary_key = getattr(ship, primary_key_name)
            if actual_primary_key == expected_primary_key:
                return ship
        else:
            return None

    def _enhance_seamis_report_with_ship_data(
        self, seamis_report: SeamisReport, ship: Ship | None
    ) -> SeamisReportWithShipData:
        combined_attributes = {
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
            combined_attributes.pop("ship_name")

        combined_attributes.update(seamis_report.dict())
        return SeamisReportWithShipData(**combined_attributes)


combine_seamis_reports_with_ships = CombineSeamisReportsWithShips()


# static type checking limitation: https://github.com/PrefectHQ/prefect/issues/4649
class CombineAccidentWithShip(Task):
    def run(  # type: ignore
        self,
        available_ships: Collection[Ship],
        enim_accidents: Collection[AccidentEnim],
    ) -> list[AccidentEnimWithShipData]:
        combined_data = []
        for enim_accident in enim_accidents:
            ship = self._find_ship(enim_accident, available_ships)
            enim_accident_with_ship_data = self._add_ship_data_to_enim_accident(
                enim_accident, ship
            )
            combined_data.append(enim_accident_with_ship_data)

        return combined_data

    def _add_ship_data_to_enim_accident(
        self, enim_accident: AccidentEnim, ship: Ship | None
    ) -> AccidentEnimWithShipData:

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

    def _find_ship(
        self, enim_accident: AccidentEnim, ship_data: Collection[Ship]
    ) -> Ship | None:
        primary_key_name = "registry_number"
        expected_primary_key = getattr(enim_accident, primary_key_name)
        for ship in ship_data:
            actual_primary_key = getattr(ship, primary_key_name)
            if actual_primary_key == expected_primary_key:
                return ship
        else:
            return None


combine_enim_accidents_with_ships = CombineAccidentWithShip()
