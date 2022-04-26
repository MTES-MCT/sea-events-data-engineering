import shelve

from .database import SHELVE_NAME
from src.repositories.enim_accidents.abc import EnimAccidentClientABC
from src.entities import AccidentEnim


class EnimAccidentClientFake(EnimAccidentClientABC):
    def get_all(self) -> list[AccidentEnim]:
        with shelve.open(SHELVE_NAME) as db:
            return [AccidentEnim(**accident) for accident in db.values()]
