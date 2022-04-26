from src.repositories.ships.abc import ShipClientABC
from src.repositories.enim_accidents.abc import EnimAccidentClientABC
from src.repositories.enim_accidents_with_ships_data.abc import EnimAccidentClientWithShipsDataABC

from config import Config

ShipClient: ShipClientABC
match Config.SHIP_CLIENT:
    case "dam_oracle":
        from src.repositories.ships.dam_oracle.client import ShipClientDamOracle
        ShipClient = ShipClientDamOracle
    case "fake":
        from src.repositories.ships.fake.client import ShipClientFake
        ShipClient = ShipClientFake
    case _:
        raise ValueError(f"Unknown ship client: {Config.SHIP_CLIENT}")

EnimAccidentClient: EnimAccidentClientABC
match Config.ENIM_ACCIDENT_CLIENT:
    case "fake":
        from src.repositories.enim_accidents.fake.client import EnimAccidentClientFake
        EnimAccidentClient = EnimAccidentClientFake
    case _:
        raise ValueError(f"Unknown enim accident client: {Config.ENIM_ACCIDENT_CLIENT}")

EnimAccidentClientWithShipsData: EnimAccidentClientWithShipsDataABC
match Config.ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT:
    case "fake":
        from src.repositories.enim_accidents_with_ships_data.fake.client import EnimAccidentClientWithShipsDataFake
        EnimAccidentClientWithShipsData = EnimAccidentClientWithShipsDataFake
    case "sqlite":
        from src.repositories.enim_accidents_with_ships_data.sqlite.client import EnimAccidentClientWithShipsDataSQLite
        EnimAccidentClientWithShipsData = EnimAccidentClientWithShipsDataSQLite
    case _:
        raise ValueError(f"Unknown enim accident with ships data client: {Config.ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT}")
