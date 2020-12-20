from tkinter import ttk, Tk, messagebox


class Output:
    def __init__(self, analysis_results):
        """Constructor

        Args:
            analysis_results: A list of output elements
        """
        self.frame = None
        self.analysis_results = analysis_results

        if self.analysis_results is not None:
            self.initialize()

    def initialize(self):
        """Create the output window and display output elements
        """

        window = Tk()
        window.title("Analysis output")

        frame = ttk.Frame(master=window)

        for idx, element in enumerate(self.analysis_results):

            render = self.confirm_render(element)

            if render is False:
                window.destroy()
                return

            element.create_output(frame, idx)

        self.frame = frame

    def destroy(self):
        self.frame.destroy()

    def pack(self):
        if self.frame is not None:
            self.frame.pack()

    def confirm_render(self,element):
        """Confirm rendering of output element from user

        Args:
            element: Output element

        Returns:
            True/False based on response
        """

        elements = element.number_of_elements_to_render()

        if elements > 100:

            msg = "The analysis has {} elements to render.".format(elements)
            msg = msg+"Are you sure you wish to render it?"

            return messagebox.askokcancel(title="Are you sure",message=msg)

        return True
