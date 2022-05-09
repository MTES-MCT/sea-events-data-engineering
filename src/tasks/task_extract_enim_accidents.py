from prefect import Task

from src.entities import AccidentEnim
from src.repositories import EnimAccidentClientABC


class ExtractEnimAccidents(Task):
    def run(self, enim_accident_client: EnimAccidentClientABC) -> list[AccidentEnim]:  # type: ignore
        return enim_accident_client.get_all()


extract_enim_accidents = ExtractEnimAccidents()
