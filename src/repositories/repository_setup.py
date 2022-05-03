from src.repositories import enim_accidents_with_ships_data, enim_accidents, ships
from config import Config


def repository_setup(
    enim_accidents_with_ships_data_implementation: str = Config.ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT,
    enim_accidents_implementation: str = Config.ENIM_ACCIDENT_CLIENT,
    ships_implementation: str = Config.SHIP_CLIENT,
):
    """
    Initialize the database and restore initial data and state.
    """
    enim_accidents_with_ships_data.repository_setup(
        enim_accidents_with_ships_data_implementation
    )
    enim_accidents.repository_setup(enim_accidents_implementation)
    ships.repository_setup(ships_implementation)


if __name__ == "__main__":
    repository_setup()
