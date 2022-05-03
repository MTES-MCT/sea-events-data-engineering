import shelve
import json
from pathlib import Path

SHELVE_NAME = "enim_accidents.db.shelve"


def repository_setup():
    """
    Initialize the database and remove existing data.
    """
    fake_data_relative_location = "../fake_data.json"
    cwd = Path(__file__).resolve().parent
    with open(f"{cwd}/{fake_data_relative_location}", "r") as fake_data_file:
        enim_accidents = json.load(fake_data_file)

    with shelve.open(SHELVE_NAME) as opened_shelve:
        opened_shelve.clear()
        for enim_accident in enim_accidents:
            opened_shelve[str(enim_accident["registry_number"])] = enim_accident
