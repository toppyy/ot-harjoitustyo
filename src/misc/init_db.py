
def drop_tables(connection):
    """Drop tables in database

    Args:
        connection: db-connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists datasets;
    ''')

    connection.commit()


def create_tables(connection):
    """Creates tables in database

    Args:
        connection: db-connection
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table datasets (
            id integer primary key autoincrement,
            dataset_parameters text
        );
    ''')

    connection.commit()


def initialize_database(connection):
    """Inits the database by dropping and creating relevant tables

    Args:
        connection: db-connection
    """

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    from db_connection import get_database_connection

    initialize_database(get_database_connection())
