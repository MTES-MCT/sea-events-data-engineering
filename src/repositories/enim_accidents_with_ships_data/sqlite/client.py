from sqlalchemy.orm import Session

from .database import engine, AccidentEnimWithShipDataTable
from src.repositories.enim_accidents_with_ships_data.abc import (
    EnimAccidentWithShipsDataClientABC,
)
from src.entities import AccidentEnimWithShipData


class EnimAccidentClientWithShipsDataSQLite(EnimAccidentWithShipsDataClientABC):
    def create_many(self, data_to_load: list[AccidentEnimWithShipData]) -> None:
        with Session(engine) as session:
            for data in data_to_load:
                self._create_one(session, data)
            session.commit()

    def _create_one(
        self, session: Session, data_to_load: AccidentEnimWithShipData
    ) -> None:
        session.add(AccidentEnimWithShipDataTable(**data_to_load.dict()))
