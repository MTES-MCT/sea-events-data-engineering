from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///seamis_reports_with_ships_data.db.sqlite3")
Base = declarative_base()


class SeamisReportWithShipDataTable(Base):  # type: ignore
    __tablename__ = "seamis_report_with_ship_data"
    report_identifier = Column(String, primary_key=True)
    registry_number = Column(String)
    occurrence_date = Column(String, nullable=False)
    num_version = Column(Integer)
    IMO_number = Column(Integer)
    flag_state = Column(String)
    gross_tonnage = Column(Integer)
    built_year = Column(Integer)
    hull_material = Column(String)
    propulsion_type = Column(String)
    length_overall = Column(Integer)
    national_location = Column(String)
    navigation_type_navpro = Column(String)
    navigation_type_gina = Column(String)
    ship_type = Column(String)


def repository_setup():
    """
    Initialize the database and remove existing data.
    """
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
