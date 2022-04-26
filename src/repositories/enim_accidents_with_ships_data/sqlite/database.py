from sqlalchemy import Column, create_engine, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AccidentEnimWithShipDataTable(Base):
    __tablename__ = 'accident_enim_with_ship_data'
    registry_number = Column(String, primary_key=True)
    employer_number = Column(String)
    SIRET = Column(String)
    is_commute_accident = Column(Boolean)
    is_with_work_interruption = Column(Boolean)
    event_date = Column(String)
    offloading_date = Column(String)
    ship_name = Column(String)
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


engine = create_engine('sqlite:///enim_accidents_with_ships_data.db')
Base.metadata.create_all(engine)
