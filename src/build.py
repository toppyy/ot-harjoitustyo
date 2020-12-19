
from misc.db_connection import get_database_connection
from misc.init_db       import initialize_database

# Init db

initialize_database(get_database_connection())
