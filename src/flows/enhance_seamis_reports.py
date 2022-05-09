from prefect import Flow

from src import tasks

enhance_seamis_reports_flow = Flow("enhance_seamis_reports_flow")

enhance_seamis_reports_flow.set_dependencies(
    task=tasks.extract_ship_data_from_seamis_reports,
    keyword_tasks=dict(seamis_reports=tasks.extract_seamis_reports),
)
enhance_seamis_reports_flow.set_dependencies(
    task=tasks.combine_seamis_reports_with_ships,
    keyword_tasks=dict(
        seamis_reports=tasks.extract_seamis_reports,
        available_ships=tasks.extract_ship_data_from_seamis_reports,
    ),
)
enhance_seamis_reports_flow.set_dependencies(
    task=tasks.load_seamis_reports_with_ship,
    keyword_tasks=dict(enhanced_seamis_reports=tasks.combine_seamis_reports_with_ships),
)
