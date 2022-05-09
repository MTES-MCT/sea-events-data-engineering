from prefect import Task

from src.repositories import SeamisReportClient
from src.entities import SeamisReport


class ExtractSeamisReports(Task):

    _seamis_client = SeamisReportClient()

    def run(self) -> list[SeamisReport]:  # type: ignore
        return self._seamis_client.get_all()


extract_seamis_reports = ExtractSeamisReports()
