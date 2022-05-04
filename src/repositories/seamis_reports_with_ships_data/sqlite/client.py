from sqlalchemy.orm import Session

from .database import engine, SeamisReportWithShipDataTable
from src.repositories.seamis_reports_with_ships_data.abc import (
    SeamisReportWithShipDataClientABC,
)
from src.entities import SeamisReportWithShipData


class SeamisReportWithShipDataClientSQLite(SeamisReportWithShipDataClientABC):
    def create_many(self, data_to_load: list[SeamisReportWithShipData]) -> None:
        with Session(engine) as session:
            for data in data_to_load:
                self._create_one(session, data)
            session.commit()

    def _create_one(
        self, session: Session, data_to_load: SeamisReportWithShipData
    ) -> None:
        session.add(SeamisReportWithShipDataTable(**data_to_load.dict()))
