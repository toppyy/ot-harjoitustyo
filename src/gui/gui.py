from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu, filedialog

from gui.analysis.summary           import Summary
from gui.analysis.frequency_table   import Frequencytable
from gui.data_input                 import DataInput
from misc.load_file_as_dataset      import load_file_as_dataset, load_exampledata


class GUI:

    def __init__(self, root, StatAnalyzer):
        self.root = root
        self.stat_analyzer = StatAnalyzer
        self.available_commands = ['Frequency table', 'Summary']

    def start(self):
        frame = ttk.Frame(master=self.root)


        for idx, text in enumerate(self.available_commands):
            btn = ttk.Button(master=frame, text=text,
                             command=lambda text=text: self.init_setup(text))
            btn.grid(row=idx+1, column=0)

        frame.pack()

        self.construct_menu()

    def construct_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File', menu=filemenu)

        filemenu.add_command(label='Load CSV-file..',command=self.open_datainput)
        filemenu.add_command(label='Load exampledata', command=self.load_exampledata)

        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)

    def open_file(self):
        path = filedialog.askopenfilename()
        data = load_file_as_dataset(path)
        self.stat_analyzer.set_dataset(data)

    def open_datainput(self):

        DataInput(self.stat_analyzer.set_dataset)



    def load_exampledata(self):
        self.stat_analyzer.set_dataset(load_exampledata())

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
