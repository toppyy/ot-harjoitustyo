from tkinter import messagebox, Menu

from gui.data_input         import DataInput
from misc.load_exampledata  import load_exampledata
from gui.homeview           import Homeview

class GUI:

    def __init__(self,window, StatAnalyzer):
        self.root = window
        self.stat_analyzer = StatAnalyzer
        self.stat_analyzer.set_gui(self)

        self.analyses = self.stat_analyzer.get_available_analyses()
        self.current_view = None

    def start(self):
        self.construct_menu()
        self.show_home()
        self.root.mainloop()

    def construct_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)

        menu.add_cascade(label='File', menu=filemenu)
        menu.add_command(label='Home', command=self.show_home)

        filemenu.add_command(label='Load CSV-file..',command=self.open_datainput)
        filemenu.add_command(label='Load exampledata', command=self.load_exampledata)

        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)


    def open_datainput(self):

        DataInput(self.stat_analyzer.set_dataset, gui=self)

    def load_exampledata(self):
        self.stat_analyzer.set_dataset(load_exampledata(gui=self))

    def show_warning(self,warningmsg):
        messagebox.showwarning(message=warningmsg)

    def show_error(self,warningmsg):
        messagebox.showerror(message=warningmsg)

    def ask_are_you_sure(self,question):
        return messagebox.askokcancel(title="Are you sure",message=question)

    def show_setup(self,analysis_name):

        analysis = self.analyses[analysis_name]

        view = analysis(
            stat_analyzer=self.stat_analyzer,
            window=self.root,
            show_error=self.show_error
        )
        self.change_view(view)

    def change_view(self,new_view):

        self.hide_current_view()
        self.current_view = new_view
        self.current_view.pack()

    def show_home(self):

        view = Homeview(
            self.root,
            self.analyses,
            self.show_setup,
            self.stat_analyzer,
            self.show_error
        )
        self.change_view(view)


    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None
