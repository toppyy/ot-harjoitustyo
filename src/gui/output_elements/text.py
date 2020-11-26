from tkinter import ttk


class Text:

    def __init__(self,text=None):
        self.text = text

    def get_text(self):
        return self.text

    def set_text(self,text):
        self.text = text


    def get_output(self, master_to_be):
        return ttk.Label(master=master_to_be, text = self.text)
    