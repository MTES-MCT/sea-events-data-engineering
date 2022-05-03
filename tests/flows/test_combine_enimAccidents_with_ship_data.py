from prefect.core.edge import Edge

from src.flows import combine_enim_accidents_with_ship_flow
from src import tasks


class TestCombineEnimAccidentsWithShipData:
    def test_flow_is_running(self, reset_repository):
        flow_state = combine_enim_accidents_with_ship_flow.run()
        assert flow_state.is_successful()

    def test_execution_graph_is_ok(self, reset_repository):
        """
        - Gather the ENIM accidents to injest
        - From the ENIM accidents to inject, gather related ships that can be found
        - From the ENIM accidents to inject and their related ships, combine there informations
        - Load the combined informations into the storage
        """
        expected_edges = {
            Edge(
                tasks.extract_enim_accidents,
                tasks.combine_enim_accidents_with_ships,
                "enim_accidents",
            ),
            Edge(
                tasks.extract_enim_accidents,
                tasks.extract_ships_data,
                "enim_accidents",
            ),
            Edge(
                tasks.extract_ships_data,
                tasks.combine_enim_accidents_with_ships,
                "available_ships",
            ),
            Edge(
                tasks.combine_enim_accidents_with_ships,
                tasks.load_enim_accidents_with_ship,
                "enim_accidents_with_ship_data",
            ),
        }

        assert len(expected_edges) == len(combine_enim_accidents_with_ship_flow.edges)
        for expected_edge in expected_edges:
            assert expected_edge in combine_enim_accidents_with_ship_flow.edges
