from prefect import Task

from src.entities import SeamisReportWithShipData
from src.repositories import SeamisReportWithShipDataClient


class LoadSeamisReportsWithShip(Task):
    _seamis_report_with_ship_data_client = SeamisReportWithShipDataClient()

    def run(self, enhanced_seamis_reports: list[SeamisReportWithShipData]) -> None:  # type: ignore
        self.logger.info(f"Creating {enhanced_seamis_reports} records")
        self._seamis_report_with_ship_data_client.create_many(enhanced_seamis_reports)


load_seamis_reports_with_ship = LoadSeamisReportsWithShip()
