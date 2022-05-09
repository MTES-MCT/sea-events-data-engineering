from prefect import Task

from src.entities import AccidentEnim
from src.repositories import enim_accidents_client_factory


class ExtractEnimAccidents(Task):
    def run(self, enim_accident_client_implementation: str) -> list[AccidentEnim]:  # type: ignore
        enim_accident_client = enim_accidents_client_factory(
            enim_accident_client_implementation
        )
        return enim_accident_client.get_all()


extract_enim_accidents = ExtractEnimAccidents()
