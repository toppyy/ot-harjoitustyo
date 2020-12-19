
import os
import sqlite3
from pathlib import Path

dirname = Path(os.path.dirname(__file__))
dirname = dirname.parent
dirname = dirname.parent

dbfilename  = os.path.join(dirname, "data", "datasets.sqlite")


connection = sqlite3.connect(dbfilename)


def get_database_connection():
    return connection
