from misc.init_db import initialize_database
from misc.db_connection import get_database_connection


def pytest_configure():
    initialize_database(get_database_connection())
