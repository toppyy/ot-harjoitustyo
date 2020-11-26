from tkinter import ttk, Tk


class Error:

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def throw(self):

        window = Tk()
        window.title("Analysis setup")

        frame = ttk.Frame(master=window)

        label = ttk.Label(master=frame, text=self.error_msg)
        label.grid(row=0, column=0)

        frame.pack()
