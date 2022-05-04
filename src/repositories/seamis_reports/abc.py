from abc import ABC, abstractmethod

from src.entities import SeamisReport


class SeamisReportClientABC(ABC):
    @abstractmethod
    def get_all(self) -> list[SeamisReport]:
        pass
