from abc import ABC, abstractmethod

from src.entities import AccidentEnim


class EnimAccidentClientABC(ABC):
    @abstractmethod
    def get_all(self) -> list[AccidentEnim]:
        pass
