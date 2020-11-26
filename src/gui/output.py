from tkinter import ttk, Tk


class Output:
    def __init__(self, analysis):
        self.frame = None
        self.analysis = analysis
        self.initialize()

    def initialize(self):

        window = Tk()
        window.title("Analysis output")

        self.frame = ttk.Frame(master=window)
        for idx, element in enumerate(self.analysis):
            tmp = element.get_output(self.frame)
            tmp.grid(row=idx, column=0)

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()
