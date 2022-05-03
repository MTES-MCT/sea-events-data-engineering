import shelve
import json
from pathlib import Path

SHELVE_NAME = "ships.db.shelve"


def repository_setup():
    fake_data_relative_location = "../fake_data.json"
    cwd = Path(__file__).resolve().parent
    with open(f"{cwd}/{fake_data_relative_location}", "r") as fake_data_file:
        ships = json.load(fake_data_file)

    with shelve.open(SHELVE_NAME) as opened_shelve:
        opened_shelve.clear()
        for ship in ships:
            opened_shelve[str(ship["registry_number"])] = ship
