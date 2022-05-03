from prefect import Task

from src.entities import AccidentEnim
from src.repositories import EnimAccidentClient


class ExtractEnimAccidents(Task):

    _enim_accident_client = EnimAccidentClient()

    def run(self) -> list[AccidentEnim]:  # type: ignore
        return self._enim_accident_client.get_all()


extract_enim_accidents = ExtractEnimAccidents()
