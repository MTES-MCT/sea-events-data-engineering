from .fake.client import EnimAccidentClientFake
from .abc import EnimAccidentClientABC
from config import Config


def repository_setup(repository_implementation: str):
    """
    Initialize the database and restore initial data and state.
    """
    match repository_implementation:
        case "fake":
            from .fake.database import repository_setup as fake_repository_setup

            fake_repository_setup()
        case _:
            raise ValueError(
                f"Unknown repository_implementation: {repository_implementation}"
            )


def client_factory(
    repository_implementation: str = Config.ENIM_ACCIDENT_CLIENT,
) -> EnimAccidentClientABC:
    match repository_implementation:
        case "fake":
            from src.repositories.enim_accidents.fake.client import (
                EnimAccidentClientFake,
            )

            return EnimAccidentClientFake()
        case _:
            raise ValueError(
                f"Unknown enim accident client: {repository_implementation}"
            )
