from abc import ABC, abstractmethod

from src.entities import SeamisReportWithShipData


class SeamisReportWithShipDataClientABC(ABC):
    @abstractmethod
    def create_many(self, data_to_load: list[SeamisReportWithShipData]) -> None:
        pass
