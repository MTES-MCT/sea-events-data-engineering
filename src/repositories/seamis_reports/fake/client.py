import shelve

from .database import SHELVE_NAME
from src.repositories.seamis_reports.abc import SeamisReportClientABC
from src.entities import SeamisReport


class SeamisReportClientFake(SeamisReportClientABC):
    def get_all(self) -> list[SeamisReport]:
        with shelve.open(SHELVE_NAME) as opened_shelf:
            return [SeamisReport(**seamis_report) for seamis_report in opened_shelf.values()]  # type: ignore
