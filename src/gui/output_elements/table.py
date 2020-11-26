
from tkinter import ttk

class Table:

    def __init__(self,data):
        self.data = data

    def get_output(self,master_to_be,row_idx):

        row_idx = row_idx
        col_idx = -1

        columns = len(self.data[0])

        for row in self.data:
            row_idx = row_idx + 1

            for col in row:
                col_idx = col_idx + 1

                cell = ttk.Entry(master=master_to_be,width=20)
                cell.grid(row=row_idx,column= ( col_idx % columns )   )
                cell.insert(0, col)

