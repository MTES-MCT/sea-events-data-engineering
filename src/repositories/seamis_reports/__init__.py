from config import Config
from .abc import SeamisReportClientABC
from src.entities import SeamisReport


def repository_setup(repository_implementation: str):
    """
    Initialize the database and restore initial data and state.
    """
    match repository_implementation:
        case "fake":
            from .fake.database import repository_setup as fake_repository_setup

            fake_repository_setup()
        case _:
            raise ValueError(
                f"Unknown repository_implementation: {repository_implementation}"
            )


class SeamisReportClient(SeamisReportClientABC):
    def __init__(self, seamis_report_repository: str = Config.SEAMIS_REPORT_CLIENT):
        self._implementation: SeamisReportClientABC = NotImplemented
        match seamis_report_repository:
            case "fake":
                from src.repositories.seamis_reports.fake.client import (
                    SeamisReportClientFake,
                )

                self._implementation = SeamisReportClientFake()
            case _:
                raise ValueError(
                    f"Unknown seamis report client: {Config.SEAMIS_REPORT_CLIENT}"
                )

    def get_all(self) -> list[SeamisReport]:
        return self._implementation.get_all()
