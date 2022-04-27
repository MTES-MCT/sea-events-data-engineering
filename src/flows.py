from prefect import Flow

from src import tasks

combine_enim_accidents_with_ship_flow = Flow("combine_enim_accidents_with_ship_flow")

combine_enim_accidents_with_ship_flow.add_edge(
    tasks.extract_enim_accidents,
    tasks.extract_ships_data,
    "enim_accidents",
)
combine_enim_accidents_with_ship_flow.add_edge(
    tasks.extract_enim_accidents,
    tasks.combine_enim_accidents_with_ships,
    "enim_accidents",
)
combine_enim_accidents_with_ship_flow.add_edge(
    tasks.extract_ships_data,
    tasks.combine_enim_accidents_with_ships,
    "ship_data",
)
combine_enim_accidents_with_ship_flow.add_edge(
    tasks.combine_enim_accidents_with_ships,
    tasks.load_enim_accidents_with_ship,
    "enim_accidents_with_ship_data",
)
