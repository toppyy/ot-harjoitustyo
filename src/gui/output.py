from tkinter import ttk, Tk


class Output:
    def __init__(self, analysis):
        self.frame = None
        self.analysis = analysis

        if self.analysis is not None:
            self.initialize()

    def initialize(self):

        window = Tk()
        window.title("Analysis output")

        self.frame = ttk.Frame(master=window)

        for idx, element in enumerate(self.analysis):
            element.get_output(self.frame, idx)

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        if self.frame is not None:
            self.frame.pack()
