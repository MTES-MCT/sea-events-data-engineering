VALID_SHIP_CLIENT_TYPES = {"dam_oracle", "fake"}
VALID_ENIM_ACCIDENT_CLIENT_TYPES = {"fake"}
VALID_ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT_TYPES = {"fake", "sqlite"}
VALID_SEAMIS_REPORT_CLIENT_TYPES = {"fake"}
VALID_SEAMIS_REPORT_WITH_SHIPS_DATA_CLIENT_TYPES = {"fake", "sqlite"}


class Config:
    SHIP_CLIENT = "fake"
    ENIM_ACCIDENT_CLIENT = "fake"
    ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT = "sqlite"
    SEAMIS_REPORT_CLIENT = "fake"
    SEAMIS_REPORT_WITH_SHIPS_DATA_CLIENT = "sqlite"


if Config.ENIM_ACCIDENT_CLIENT not in VALID_ENIM_ACCIDENT_CLIENT_TYPES:
    raise ValueError(f"Unknown enim accident client: {Config.ENIM_ACCIDENT_CLIENT}")

if Config.SHIP_CLIENT not in VALID_SHIP_CLIENT_TYPES:
    raise ValueError(f"Unknown ship client: {Config.SHIP_CLIENT}")

if Config.ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT not in VALID_ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT_TYPES:
    raise ValueError(f"Unknown enim accident with ships data client: {Config.ENIM_ACCIDENT_WITH_SHIPS_DATA_CLIENT}")

if Config.SEAMIS_REPORT_CLIENT not in VALID_SEAMIS_REPORT_CLIENT_TYPES:
    raise ValueError(f"Unknown seamis report client: {Config.SEAMIS_REPORT_CLIENT}")

if Config.SEAMIS_REPORT_WITH_SHIPS_DATA_CLIENT not in VALID_SEAMIS_REPORT_WITH_SHIPS_DATA_CLIENT_TYPES:
    raise ValueError(f"Unknown seamis report with ships data client: {Config.SEAMIS_REPORT_WITH_SHIPS_DATA_CLIENT}")
