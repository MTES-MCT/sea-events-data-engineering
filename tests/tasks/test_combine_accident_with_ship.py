import pytest
from prefect import Task

from src.tasks.tasks_enhance_with_ships import (
    CombineAccidentWithShip,
    CombineSeamisReportsWithShips,
)
from src.entities import (
    AccidentEnimWithShipData,
    Ship,
    SeamisReport,
    SeamisReportWithShipData,
)


class TestCombineAccidentWithShip:
    def test_is_prefect_task(self):
        assert isinstance(CombineAccidentWithShip(), Task)

    @pytest.mark.parametrize(
        "valid_enim_accident_test_case",
        ["valid_enim_accident_test_case_1", "valid_enim_accident_test_case_2"],
        indirect=True,
    )
    def test_ok(self, valid_enim_accident_test_case):
        combine_accident_with_ship = CombineAccidentWithShip()
        expected_combined_data = valid_enim_accident_test_case["accidents + ships"]

        task_result = combine_accident_with_ship.run(
            valid_enim_accident_test_case["ships"],
            valid_enim_accident_test_case["accidents"],
        )

        assert task_result == expected_combined_data

    def test_no_matching_ship(self, valid_enim_accident_test_case_1):

        combine_accident_with_ship = CombineAccidentWithShip()
        accident = valid_enim_accident_test_case_1["accidents"][0]
        accidents = [accident]
        ships = []
        expected_result = [
            AccidentEnimWithShipData(
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
                ship_type=None,
            )
        ]

        task_result = combine_accident_with_ship.run(ships, accidents)

        assert task_result == expected_result


class TestCombineSeamisReportsWithShips:
    def test_is_prefect_task(self):
        assert isinstance(CombineSeamisReportsWithShips(), Task)

    def test_ok(self):
        combine_seamis_reports_with_ships = CombineSeamisReportsWithShips()
        seamis_reports = [
            SeamisReport(
                registry_number=931196,
                occurrence_date="2021/08/13",
            )
        ]
        ships = [
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
                ship_type="",
            )
        ]
        expected_result = [
            SeamisReportWithShipData(
                registry_number=931196,
                occurrence_date="2021/08/13",
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
                ship_type="",
            )
        ]

        task_result = combine_seamis_reports_with_ships.run(ships, seamis_reports)

        assert task_result == expected_result

    def test_no_matching_ship(self):
        combine_seamis_reports_with_ships = CombineSeamisReportsWithShips()
        seamis_reports = [
            SeamisReport(
                registry_number=931196,
                occurrence_date="2021/08/13",
            )
        ]
        ships = []
        expected_result = [
            SeamisReportWithShipData(
                registry_number=931196,
                occurrence_date="2021/08/13",
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
                ship_type=None,
            )
        ]

        task_result = combine_seamis_reports_with_ships.run(ships, seamis_reports)

        assert task_result == expected_result

    def test_seamis_report_without_registry_number(self):
        combine_seamis_reports_with_ships = CombineSeamisReportsWithShips()
        seamis_reports = [
            SeamisReport(
                registry_number=None,
                occurrence_date="2021/08/13",
            )
        ]
        ships = []
        expected_result = [
            SeamisReportWithShipData(
                registry_number=None,
                occurrence_date="2021/08/13",
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
                ship_type=None,
            )
        ]

        task_result = combine_seamis_reports_with_ships.run(ships, seamis_reports)

        assert task_result == expected_result
