import shelve

SHELVE_NAME = "seamis_reports_with_ships_data.db.shelve"


def repository_setup():
    with shelve.open(SHELVE_NAME) as opened_shelve:
        opened_shelve.clear()
