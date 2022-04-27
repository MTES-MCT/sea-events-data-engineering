from config import Config
from .abc import EnimAccidentClientABC
from src.entities import AccidentEnim


class EnimAccidentClient(EnimAccidentClientABC):
    def __init__(self, enim_accidents_repository: str = Config.ENIM_ACCIDENT_CLIENT):
        self._implementation: EnimAccidentClientABC = NotImplemented
        match enim_accidents_repository:
            case "fake":
                from src.repositories.enim_accidents.fake.client import (
                    EnimAccidentClientFake,
                )

                self._implementation = EnimAccidentClientFake()
            case _:
                raise ValueError(
                    f"Unknown enim accident client: {Config.ENIM_ACCIDENT_CLIENT}"
                )

    def get_all(self) -> list[AccidentEnim]:
        print(self._implementation)
        return self._implementation.get_all()
