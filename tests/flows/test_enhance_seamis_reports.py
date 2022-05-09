from prefect.core.edge import Edge

from src.flows import enhance_seamis_reports_flow
from src import tasks


class TestEnhanceSeamisReports:
    def test_flow_is_running(self, reset_repository):
        flow_state = enhance_seamis_reports_flow.run()
        assert flow_state.is_successful()

    def test_execution_graph_is_ok(self, reset_repository):
        """
        - Gather seamis reports to process
        - Gather ships involved in sea events
        """

        expected_edges = {
            Edge(
                tasks.extract_seamis_reports,
                tasks.extract_ship_data_from_seamis_reports,
                "seamis_reports",
            ),
            Edge(
                tasks.extract_ship_data_from_seamis_reports,
                tasks.combine_seamis_reports_with_ships,
                "available_ships",
            ),
            Edge(
                tasks.extract_seamis_reports,
                tasks.combine_seamis_reports_with_ships,
                "seamis_reports",
            ),
            Edge(
                tasks.combine_seamis_reports_with_ships,
                tasks.load_seamis_reports_with_ship,
                "enhanced_seamis_reports",
            ),
        }

        assert len(expected_edges) == len(enhance_seamis_reports_flow.edges)
        for expected_edge in expected_edges:
            assert expected_edge in enhance_seamis_reports_flow.edges
