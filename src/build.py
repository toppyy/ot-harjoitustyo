
from misc.db_connection import get_database_connection
from misc.init_db       import initialize_database

# Init db

try:
    initialize_database(get_database_connection())
except Exception as err:
    print('Database was not created due to an error ({})'.format(str(err)))

print('build done')
