from typing import Collection

from prefect import Task

from src.entities import AccidentEnim, Ship, SeamisReport
from src.repositories import ShipClient


class ExtractShipDataFromEnimAccidents(Task):

    _ship_client = ShipClient()

    def run(self, enim_accidents: Collection[AccidentEnim]) -> list[Ship]:  # type: ignore
        registry_numbers = [
            str(accident.registry_number) for accident in enim_accidents
        ]
        return self._ship_client.get_by_registry_number(registry_numbers)


extract_ship_data_from_enim_accidents = ExtractShipDataFromEnimAccidents()


class ExtractShipDataFromSeamisReports(Task):

    _ship_client = ShipClient()

    def run(self, seamis_reports: Collection[SeamisReport]) -> list[Ship]:  # type: ignore
        self.logger.info("Extracting ship data from seamis reports")
        self.logger.info(f"Seamis reports: {seamis_reports}")
        registry_numbers = [
            str(seamis_report.registry_number) for seamis_report in seamis_reports
        ]
        return self._ship_client.get_by_registry_number(registry_numbers)


extract_ship_data_from_seamis_reports = ExtractShipDataFromSeamisReports()
