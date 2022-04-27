import shelve
import json
from pathlib import Path

SHELVE_NAME = "enim_accidents.db"

fake_data_relative_location = "../fake_data.json"
cwd = Path(__file__).resolve().parent
with open(f"{cwd}/{fake_data_relative_location}", "r") as fake_data_file:
    enim_accidents = json.load(fake_data_file)

with shelve.open(SHELVE_NAME) as db:
    db.clear()
    for enim_accident in enim_accidents:
        db[str(enim_accident["registry_number"])] = enim_accident
