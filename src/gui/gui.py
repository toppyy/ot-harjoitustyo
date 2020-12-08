from tkinter import ttk, Tk, messagebox, Menu

from gui.analysis_setup.summary           import Summary
from gui.analysis_setup.frequencytable    import Frequencytable
from gui.analysis_setup.summarytable      import Summarytable
from gui.analysis_setup.scatterplot       import Scatterplot
from gui.data_input                       import DataInput
from misc.load_exampledata                import load_exampledata


class GUI:

    def __init__(self, StatAnalyzer):
        window = Tk()
        window.title("Stat analyzer")
        self.root = window
        self.stat_analyzer = StatAnalyzer
        self.available_commands = ['Frequency table', 'Summary','Summary table', 'Scatterplot']


    def start(self):
        frame = ttk.Frame(master=self.root)


        for idx, text in enumerate(self.available_commands):
            btn = ttk.Button(master=frame, text=text,
                             command=lambda text=text: self.init_setup(text))
            btn.grid(row=idx+1, column=0)

        frame.pack()

        self.construct_menu()

        self.root.mainloop()

    def construct_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)

        filemenu.add_command(label='Load CSV-file..',command=self.open_datainput)
        filemenu.add_command(label='Load exampledata', command=self.load_exampledata)

        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)


    def open_datainput(self):

        DataInput(self.stat_analyzer.set_dataset, gui=self)

    def load_exampledata(self):
        self.stat_analyzer.set_dataset(load_exampledata(gui=self))

    def init_setup(self,analysis_name):

        if not self.stat_analyzer.has_dataset():

            err_msg = 'Error: No dataset.\n'
            err_msg = err_msg + 'Try loading the example dataset.\n(File -> Load exampledata)'

            messagebox.showerror(title=None,message=err_msg)
            return

        if analysis_name == 'Summary':
            setup = Summary(self.stat_analyzer)
            setup.pack()

        if analysis_name == 'Frequency table':
            setup = Frequencytable(self.stat_analyzer)
            setup.pack()

        if analysis_name == 'Summary table':
            setup = Summarytable(self.stat_analyzer)
            setup.pack()

        if analysis_name == 'Scatterplot':
            setup = Scatterplot(self.stat_analyzer)
            setup.pack()

    def show_warning(self,warningmsg):
        messagebox.showwarning(message=warningmsg)

    def show_error(self,warningmsg):
        messagebox.showerror(message=warningmsg)
