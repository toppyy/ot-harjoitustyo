
def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists datasets;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table datasets (
            id integer primary key autoincrement,
            dataset_parameters text
        );
    ''')

    connection.commit()


def initialize_database(connection):

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    from db_connection import get_database_connection

    initialize_database(get_database_connection())
