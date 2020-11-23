from tkinter import ttk, Tk


class Output:
    def __init__(self, analysis):
        self.frame = None
        self.analysis = analysis
        self.initialize()

    def initialize(self):

        window = Tk()
        window.title("Analysis output")

        self.frame = ttk.Frame(master=window, width=1000, height=576)

        for idx, element in enumerate(self.analysis):
            tmp = ttk.Label(master=self.frame,
                            text=element["text"]+'{}'.format(element["value"]))
            tmp.grid(row=idx, column=0)

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        self.frame.pack()
