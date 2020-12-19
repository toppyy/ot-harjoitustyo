import json


class DatasetRepository:
    """Access to dataset repository (≃ parameters to open a dataset)
    """

    def __init__(self,dbcon):
        """Constructor

        Args:
            dbcon: Connection to database
        """
        self.dbcon = dbcon



    def store_dataset_parameters(self,parameters):
        """Stores dataset params into the database

        Args:
            parameters: A dictionary of parameters
        """

        cursor = self.dbcon.cursor()

        params_as_json = json.dumps(parameters)

        cursor.execute(
            'INSERT INTO datasets(dataset_parameters) VALUES(?)',
            (params_as_json,)
        )

        id_of_inserted = cursor.lastrowid

        self.dbcon.commit()

        return id_of_inserted

    def get_dataset_parameters(self,id_to_get):
        """Getter for dataset parameters

        Args:
            Id of dataset. Integer.
        """

        cursor = self.dbcon.cursor()

        cursor.execute('SELECT * FROM datasets WHERE id=?',(id_to_get,))

        dataset_params = cursor.fetchone()

        return json.loads(dataset_params[1])


    def delete_all(self):
        """Empties the repository
        """

        cursor = self.dbcon.cursor()

        cursor.execute('DELETE FROM datasets;')

        self.dbcon.commit()

    def get_all(self):
        """Returns all dataset parameters

        Returns:
            A list of dataset parameters
        """
        cursor = self.dbcon.cursor()

        parameters = []
        for row in cursor.execute('SELECT * FROM datasets ORDER BY id;'):

            parameter = {
                "id": row[0],
                "parameters": json.loads(row[1])
            }
            parameters.append(parameter)

        return parameters
