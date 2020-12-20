from tkinter import messagebox, Menu

from gui.data_input         import DataInput
from misc.load_exampledata  import load_exampledata
from gui.homeview           import Homeview

class GUI:

    def __init__(self,window, stat_analyzer, dataset_repository):
        """Initialises the GUI

        Args:
            window: Root windows
            stat_analyzer: An instance of StatAnalyzer
            dataset_repository: An instance os DatasetRepository
        """
        self.root = window
        self.stat_analyzer = stat_analyzer
        self.dataset_repository = dataset_repository

        self.analyses = self.stat_analyzer.get_available_analyses()
        self.current_view = None

        self.data_input =  DataInput(
            set_dataset=self.stat_analyzer.set_dataset,
            gui=self,
            callback=self.store_dataset_and_refresh_menu
        )


    def start(self):
        """Construct menu, create home-view and run the mainloop
        """
        self.construct_menu()
        self.show_home()
        self.root.mainloop()

    def construct_menu(self):
        """Constructs the menu for gui
        """
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)

        menu.add_cascade(label='File', menu=filemenu)
        menu.add_command(label='Home', command=self.show_home)

        filemenu.add_command(label='Load CSV-file..',command=self.open_datainput)
        filemenu.add_command(label='Load exampledata', command=self.load_exampledata)

        filemenu.add_separator()
        self.add_recent_datasets_to_menu(filemenu)

        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)

    def add_recent_datasets_to_menu(self,filemenu):
        """Display recent datasets in the menu

        Args:
            filemenu: Menu to add submenu to
        """

        submenu = Menu(filemenu)
        try:
            datasets = self.dataset_repository.get_10_recent_datasets()
        except Exception as err:
            msg = 'Recent datasets could not be loaded. Running build might help.\n'
            msg = msg + '(Err: {})'.format(err)
            self.show_error(msg)
            return

        for dataset in datasets:
            params = dataset['parameters']
            submenu.add_command(
                label=params['filename']
                ,command= lambda params=params: self.load_dataset_from_params(params)
            )

        filemenu.add_cascade(label='Recent datasets..', menu=submenu, underline=0)

    def load_dataset_from_params(self,params):
        """Loads a dataset from parameters (from dataset repository)

        Args:
            params: Parameters for reading the dataset
        """

        self.data_input.read_data(
            params['fullpath'],
            params['delimiter'],
            params['has_header'],
            params['row_limit']
        )
        self.show_home()

    def store_dataset_and_refresh_menu(self,parameters):
        """Stores a dataset to repository and re-creates the menu

        Args:
            parameters to store to repository
        """
        try:
            self.dataset_repository.store_dataset_parameters(parameters)
            self.construct_menu()
        except Exception as err:
            msg = 'Dataset could not stored. Running build might help. (Err: {})'.format(err)
            self.show_error(msg)
            return


    def load_exampledata(self):
        """Loads the example data to StatAnalyzer
        """
        self.stat_analyzer.set_dataset(load_exampledata())

    def show_warning(self,warningmsg):
        messagebox.showwarning(message=warningmsg)

    def show_error(self,warningmsg):
        messagebox.showerror(message=warningmsg)

    def ask_are_you_sure(self,question):
        return messagebox.askokcancel(title="Are you sure",message=question)



    def open_datainput(self):
        """Opens the data input window
        """
        self.data_input.init()

    def show_setup(self,analysis):
        """Shows an instance of Setup-view

        Args:
            analysis: key of the analysis for which to open setup for
        """

        setup_function = analysis['setup']

        view = setup_function(
            stat_analyzer=self.stat_analyzer,
            window=self.root,
            show_error=self.show_error,
            analysis = analysis
        )
        self.change_view(view)

    def change_view(self,new_view):
        """Hides the current view and displays the new view

        Args:
            new_view: The new view to display
        """

        self.hide_current_view()
        self.current_view = new_view
        self.current_view.pack()

    def show_home(self):
        """Displays home-view
        """

        view = Homeview(
            self.root,
            self.analyses,
            self.show_setup,
            self.stat_analyzer,
            self.show_error
        )
        self.change_view(view)


    def hide_current_view(self):
        """Hides the current view (destroys it)
        """
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None
