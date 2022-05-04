import shelve
import json
from pathlib import Path

SHELVE_NAME = "seamis_report.db.shelve"


def repository_setup():
    seamis_reports = []
    fake_data_folder_relative_path = "../fake_data"
    cwd = Path(__file__).resolve().parent
    for fake_data_path in cwd.joinpath(fake_data_folder_relative_path).glob("*.json"):
        with open(fake_data_path) as fake_data_file:
            raw_seamis_report = json.load(fake_data_file)
            seamis_report_occurrence_data = {
                "occurrence_date": raw_seamis_report["gdhAlert"],
            }
            for vehicle in raw_seamis_report.get("vehicules", [dict()]):
                seamis_report = {
                    **seamis_report_occurrence_data,
                    "registry_number": vehicle.get("immatriculation", None),
                }
                seamis_reports.append(seamis_report)

    with shelve.open(SHELVE_NAME) as opened_shelve:
        opened_shelve.clear()
        for seamis_report in seamis_reports:
            opened_shelve[str(seamis_report["registry_number"])] = seamis_report
