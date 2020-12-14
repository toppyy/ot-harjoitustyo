from tkinter import ttk


class Text:

    def __init__(self,text=None):
        self.text = text

    def get_output(self, master_to_be, row_idx):
        lbl = ttk.Label(master=master_to_be, text = self.text)
        lbl.grid(row=row_idx,column=0)

    def get_text(self):
        return self.text

    def number_of_elements_to_render(self):
        return 1
