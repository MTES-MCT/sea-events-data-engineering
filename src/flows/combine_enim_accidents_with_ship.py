from prefect import Flow, Parameter

from src import tasks
from config import Config

combine_enim_accidents_with_ship_flow = Flow("combine_enim_accidents_with_ship_flow")


enim_accident_client_param = Parameter(
    name="enim_accident_client",
    default=Config.ENIM_ACCIDENT_CLIENT,
)
combine_enim_accidents_with_ship_flow.set_dependencies(
    task=tasks.extract_enim_accidents,
    keyword_tasks=dict(enim_accident_client_implementation=enim_accident_client_param),
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
