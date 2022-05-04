from config import Config
from .abc import SeamisReportWithShipDataClientABC
from src.entities import SeamisReportWithShipData


def repository_setup(repository_implementation: str):
    """
    Initialize the database and restore initial data and state.
    """
    match repository_implementation:
        case "fake":
            from .fake.database import repository_setup as fake_repository_setup

            fake_repository_setup()
        case "sqlite":
            from .sqlite.database import repository_setup as sqlite_repository_setup

            sqlite_repository_setup()
        case _:
            raise ValueError(
                f"Unknown repository_implementation: {repository_implementation}"
            )


class SeamisReportWithShipDataClient(SeamisReportWithShipDataClientABC):
    def __init__(
        self,
        seamis_reports_with_ships_data_repository: str = Config.SEAMIS_REPORT_WITH_SHIPS_DATA_CLIENT,
    ):
        self._implementation: SeamisReportWithShipDataClientABC = NotImplemented
        match seamis_reports_with_ships_data_repository:
            case "fake":
                from src.repositories.seamis_reports_with_ships_data.fake.client import (
                    SeamisReportWithShipDataClientFake,
                )

                self._implementation = SeamisReportWithShipDataClientFake()
            case "sqlite":
                from src.repositories.seamis_reports_with_ships_data.sqlite.client import (
                    SeamisReportWithShipDataClientSQLite,
                )

                self._implementation = SeamisReportWithShipDataClientSQLite()
            case _:
                raise ValueError(
                    f"Unknown seamis report with ships data client: {Config.SEAMIS_REPORT_WITH_SHIPS_DATA_CLIENT}"
                )

    def create_many(self, data_to_load: list[SeamisReportWithShipData]) -> None:
        pass
