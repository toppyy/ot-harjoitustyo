from tkinter import ttk


class Header:

    def __init__(self,text=None):
        self.text = text

    def get_output(self, master_to_be, row_idx):
        lbl = ttk.Label(master=master_to_be, text = self.text, font=("Courier", 13))
        lbl.grid(columnspan=2,row=row_idx,column=0)

    def get_text(self):
        return self.text
