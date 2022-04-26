from pydantic import BaseModel


class Ship(BaseModel):
    registry_number: int
    ship_name: str
    num_version: int
    IMO_number: int
    flag_state: str
    gross_tonnage: int
    built_year: int
    hull_material: str
    propulsion_type: str
    length_overall: int
    national_location: str
    navigation_type_navpro: str
    navigation_type_gina: str
    ship_type: str


class AccidentEnim(BaseModel):
    registry_number: int
    employer_number: str
    SIRET: str
    is_commute_accident: bool
    is_with_work_interruption: bool
    event_date: str
    offloading_date: str | None


class AccidentEnimWithShipData(BaseModel):
    registry_number: str
    employer_number: str
    SIRET: str
    is_commute_accident: bool
    is_with_work_interruption: bool
    event_date: str
    offloading_date: str | None
    ship_name: str | None
    num_version: int | None
    IMO_number: int | None
    flag_state: str | None
    gross_tonnage: int | None
    built_year: int | None
    hull_material: str | None
    propulsion_type: str | None
    length_overall: int | None
    national_location: str | None
    navigation_type_navpro: str | None
    navigation_type_gina: str | None
    ship_type: str | None
