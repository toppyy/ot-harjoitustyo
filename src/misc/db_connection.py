
import os
import sqlite3
from pathlib import Path

dirname = Path(os.path.dirname(__file__))
dirname = dirname.parent
dirname = dirname.parent



def get_database_connection(filename='datasets.sqlite'):
    dbfilename  = os.path.join(dirname, "data", filename)
    connection = sqlite3.connect(dbfilename)
    return connection
