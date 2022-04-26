import pytest
from prefect import Task

from src.tasks.task_combine_enim_accidents_with_ships import CombineAccidentWithShip
from src.entities import AccidentEnim, Ship, AccidentEnimWithShipData


@pytest.fixture
def valid_test_case_1():
    return {
        "accidents": [AccidentEnim(
            registry_number=931194,
            employer_number="YAD0586",
            SIRET=40018768700013,
            is_commute_accident=True,
            is_with_work_interruption=True,
            event_date="2019/02/11",
            offloading_date="2019/02/11"
        )],
        "ships": [Ship(
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
            ship_type="CANOT / VEDETTE PÊCHE"
        )],
        "accidents + ships": [AccidentEnimWithShipData(
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
            ship_type="CANOT / VEDETTE PÊCHE"
        )]
    }


@pytest.fixture
def valid_test_case_2():
    return {
        "accidents": [AccidentEnim(
            registry_number=931196,
            employer_number="YAD0588",
            SIRET=35524766700024,
            is_commute_accident=False,
            is_with_work_interruption=True,
            event_date="2021/08/13",
            offloading_date="2021/08/13"
        )],
        "ships": [Ship(
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
            ship_type="CHALUTIER"
        )],
        "accidents + ships": [AccidentEnimWithShipData(
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
            offloading_date="2021/08/13"
        )]
    }


@pytest.fixture
def valid_test_case(request, valid_test_case_1, valid_test_case_2):
    match request.param:
        case "valid_test_case_1":
            return valid_test_case_1
        case "valid_test_case_2":
            return valid_test_case_2
        case _:
            raise ValueError(f"Invalid test case {request.param}")


class TestCombineAccidentWithShip:
    def test_is_prefect_task(self):
        assert isinstance(CombineAccidentWithShip(), Task)
    
    @pytest.mark.parametrize(
        'valid_test_case',
        ["valid_test_case_1", "valid_test_case_2"],
        indirect=True
    )
    def test_ok(self, valid_test_case):
        combine_accident_with_ship = CombineAccidentWithShip()
        expected_combined_data = valid_test_case['accidents + ships']

        task_result = combine_accident_with_ship.run(
            valid_test_case["ships"],
            valid_test_case["accidents"]
        )

        assert task_result == expected_combined_data

    def test_no_matching_ship(self, valid_test_case_1):

        combine_accident_with_ship = CombineAccidentWithShip()
        accident = valid_test_case_1["accidents"][0]
        accidents = [accident]
        ships = []
        expected_result = [AccidentEnimWithShipData(
            registry_number=accident.registry_number,
            employer_number=accident.employer_number,
            SIRET=accident.SIRET,
            is_commute_accident=accident.is_commute_accident,
            is_with_work_interruption=accident.is_with_work_interruption,
            event_date=accident.event_date,
            offloading_date=accident.offloading_date,
            num_version=None,
            IMO_number=None,
            flag_state=None,
            gross_tonnage=None,
            built_year=None,
            hull_material=None,
            propulsion_type=None,
            length_overall=None,
            national_location=None,
            navigation_type_navpro=None,
            navigation_type_gina=None,
            ship_type=None
        )]

        task_result = combine_accident_with_ship.run(ships, accidents)

        assert task_result == expected_result
