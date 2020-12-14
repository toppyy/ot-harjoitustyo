from tkinter import ttk, Tk, messagebox


class Output:
    def __init__(self, analysis):
        self.frame = None
        self.analysis = analysis

        if self.analysis is not None:
            self.initialize()

    def initialize(self):

        window = Tk()
        window.title("Analysis output")

        frame = ttk.Frame(master=window)

        for idx, element in enumerate(self.analysis):

            render = self.confirm_render(element)

            if render is False:
                window.destroy()
                return

            element.get_output(frame, idx)

        self.frame = frame

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        if self.frame is not None:
            self.frame.pack()

    def confirm_render(self,element):

        elements = element.number_of_elements_to_render()

        if elements > 100:

            msg = "The analysis has {} elements to render.".format(elements)
            msg = msg+"Are you sure you wish to render it?"

            return messagebox.askokcancel(title="Are you sure",message=msg)

        return True
