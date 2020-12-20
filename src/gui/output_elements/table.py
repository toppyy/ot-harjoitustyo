
from tkinter import ttk

class Table:

    def __init__(self,data):
        self.data = data

    def create_output(self,master_to_be,row_idx):
        """Creates a table from widgets

        Args:
            master_to_be: Master to bind element to
            row_idx: Index of row to bind element to
        """
        col_idx = -1

        columns = len(self.data[0])

        cells = []

        for row in self.data:
            row_idx = row_idx + 1

            for col in row:
                col_idx = col_idx + 1

                cell = ttk.Entry(master=master_to_be,width=20)
                cell.grid(row=row_idx,column= ( col_idx % columns ))
                cell.insert(0, col)
                cells.append(cell)

        return cells

    def number_of_elements_to_render(self):
        """Getter for number of cells in the table

        Returns:
            Number of cells in the table
        """
        return len(self.data)
