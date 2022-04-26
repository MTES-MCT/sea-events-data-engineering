from prefect import Task

from src.entities import AccidentEnim
from src.connectors import get_new_enim_accidents


class ExtractEnimAccidents(Task):
    
    def run(self) -> list[AccidentEnim]:
        return get_new_enim_accidents()

extract_enim_accidents = ExtractEnimAccidents()
