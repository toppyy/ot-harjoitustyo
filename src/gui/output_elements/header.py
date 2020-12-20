from tkinter import ttk


class Header:

    def __init__(self,text=None):
        self.text = text

    def create_output(self, master_to_be, row_idx):
        """Creates the output element for given text

        Args:
            master_to_be: Master to bind element to
            row_idx: Index of row to bind element to
        """
        lbl = ttk.Label(master=master_to_be, text = self.text, font=("Courier", 13))
        lbl.grid(columnspan=2,row=row_idx,column=0)

    def get_text(self):
        return self.text

    def number_of_elements_to_render(self):
        """Number of elements. By definition 1.

        Returns:
            Number of elements
        """
        return 1
