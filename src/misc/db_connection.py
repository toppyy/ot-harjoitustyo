
import os
import sqlite3
from pathlib import Path

dirname = Path(os.path.dirname(__file__))
dirname = dirname.parent
dirname = dirname.parent



def get_database_connection(filename='datasets.sqlite'):
    """Establishes a database connection

    Args:
        filename: Name of the database file. Defaults to 'datasets.sqlite'.

    Returns:
        DB-connection.
    """
    dbfilename  = os.path.join(dirname, "data", filename)
    if filename == ":memory:":
        dbfilename = filename
    connection = sqlite3.connect(dbfilename)
    return connection
