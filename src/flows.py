from prefect import Flow

from src import tasks
from src.repositories import enim_accidents_client_factory

combine_enim_accidents_with_ship_flow = Flow("combine_enim_accidents_with_ship_flow")
enim_accident_client = enim_accidents_client_factory()

combine_enim_accidents_with_ship_flow.set_dependencies(
    task=tasks.extract_enim_accidents,
    keyword_tasks=dict(enim_accident_client=enim_accident_client),
)

combine_enim_accidents_with_ship_flow.set_dependencies(
    task=tasks.extract_ship_data_from_enim_accidents,
    keyword_tasks=dict(enim_accidents=tasks.extract_enim_accidents),
)

combine_enim_accidents_with_ship_flow.set_dependencies(
    task=tasks.combine_enim_accidents_with_ships,
    keyword_tasks=dict(
        enim_accidents=tasks.extract_enim_accidents,
        available_ships=tasks.extract_ship_data_from_enim_accidents,
    ),
)

combine_enim_accidents_with_ship_flow.set_dependencies(
    task=tasks.load_enim_accidents_with_ship,
    keyword_tasks=dict(
        enim_accidents_with_ship_data=tasks.combine_enim_accidents_with_ships
    ),
)

enhance_seamis_reports_flow = Flow("enhance_seamis_reports_flow")

enhance_seamis_reports_flow.add_edge(
    tasks.extract_seamis_reports,
    tasks.extract_ship_data_from_seamis_reports,
    "seamis_reports",
)
enhance_seamis_reports_flow.add_edge(
    tasks.extract_ship_data_from_seamis_reports,
    tasks.combine_seamis_reports_with_ships,
    "available_ships",
)
enhance_seamis_reports_flow.add_edge(
    tasks.extract_seamis_reports,
    tasks.combine_seamis_reports_with_ships,
    "seamis_reports",
)
enhance_seamis_reports_flow.add_edge(
    tasks.combine_seamis_reports_with_ships,
    tasks.load_seamis_reports_with_ship,
    "enhanced_seamis_reports",
)
