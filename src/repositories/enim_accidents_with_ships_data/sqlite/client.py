from sqlalchemy.orm import Session

from .database import engine, AccidentEnimWithShipDataTable
from src.repositories.enim_accidents_with_ships_data.abc import EnimAccidentClientWithShipsDataABC
from src.entities import AccidentEnimWithShipData

class EnimAccidentClientWithShipsDataSQLite(EnimAccidentClientWithShipsDataABC):

    def create(self, data_to_load: AccidentEnimWithShipData) -> None:
        with Session(engine) as session:
            session.add(AccidentEnimWithShipDataTable(
                **data_to_load.dict()
            ))
            session.commit()
