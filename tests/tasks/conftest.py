import pytest

from src.entities import AccidentEnimWithShipData, Ship, AccidentEnim


@pytest.fixture
def valid_enim_accident_test_case_1():
    return {
        "accidents": [
            AccidentEnim(
                registry_number=931194,
                employer_number="YAD0586",
                SIRET=40018768700013,
                is_commute_accident=True,
                is_with_work_interruption=True,
                event_date="2019/02/11",
                offloading_date="2019/02/11",
            )
        ],
        "ships": [
            Ship(
                registry_number=931194,
                ship_name="La mouette",
                num_version=3,
                IMO_number=8731019,
                flag_state="France",
                gross_tonnage=140,
                built_year=2010,
                hull_material="aluminium",
                propulsion_type="explosion",
                length_overall=22,
                national_location="Saint Nazaire",
                navigation_type_navpro="",
                navigation_type_gina="NC-NAVIGATION COTIERE",
                ship_type="CANOT / VEDETTE PÊCHE",
            )
        ],
        "accidents + ships": [
            AccidentEnimWithShipData(
                registry_number=931194,
                employer_number="YAD0586",
                SIRET=40018768700013,
                is_commute_accident=True,
                is_with_work_interruption=True,
                event_date="2019/02/11",
                offloading_date="2019/02/11",
                ship_name="La mouette",
                num_version=3,
                IMO_number=8731019,
                flag_state="France",
                gross_tonnage=140,
                built_year=2010,
                hull_material="aluminium",
                propulsion_type="explosion",
                length_overall=22,
                national_location="Saint Nazaire",
                navigation_type_navpro="",
                navigation_type_gina="NC-NAVIGATION COTIERE",
                ship_type="CANOT / VEDETTE PÊCHE",
            )
        ],
    }


@pytest.fixture
def valid_enim_accident_test_case_2():
    return {
        "accidents": [
            AccidentEnim(
                registry_number=931196,
                employer_number="YAD0588",
                SIRET=35524766700024,
                is_commute_accident=False,
                is_with_work_interruption=True,
                event_date="2021/08/13",
                offloading_date="2021/08/13",
            )
        ],
        "ships": [
            Ship(
                registry_number=931196,
                ship_name="Le Cormoran",
                num_version=1,
                IMO_number=8731021,
                flag_state="France",
                gross_tonnage=117,
                built_year=1986,
                hull_material="acier",
                propulsion_type="explosion",
                length_overall=20,
                national_location="Jobourg",
                navigation_type_navpro="",
                navigation_type_gina="NC-NAVIGATION COTIERE",
                ship_type="CHALUTIER",
            )
        ],
        "accidents + ships": [
            AccidentEnimWithShipData(
                registry_number=931196,
                ship_name="Le Cormoran",
                num_version=1,
                IMO_number=8731021,
                flag_state="France",
                gross_tonnage=117,
                built_year=1986,
                hull_material="acier",
                propulsion_type="explosion",
                length_overall=20,
                national_location="Jobourg",
                navigation_type_navpro="",
                navigation_type_gina="NC-NAVIGATION COTIERE",
                ship_type="CHALUTIER",
                employer_number="YAD0588",
                SIRET=35524766700024,
                is_commute_accident=False,
                is_with_work_interruption=True,
                event_date="2021/08/13",
                offloading_date="2021/08/13",
            )
        ],
    }


@pytest.fixture
def valid_enim_accident_test_case(
    request, valid_enim_accident_test_case_1, valid_enim_accident_test_case_2
):
    match request.param:
        case "valid_enim_accident_test_case_1":
            return valid_enim_accident_test_case_1
        case "valid_enim_accident_test_case_2":
            return valid_enim_accident_test_case_2
        case _:
            raise ValueError(f"Invalid test case {request.param}")
