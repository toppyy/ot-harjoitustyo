import re
from tkinter import ttk, Tk, filedialog, Radiobutton, BooleanVar
from file_access import FileAccess
from dataset import Dataset

class DataInput:
    """Class responsible for the view controlling loading datasets
    """

    def __init__(self, set_dataset, gui, callback):
        """Constructor

        Args:
            set_dataset: function to be called once the dataset is created
            gui: reference to the gui creating the instance
            callback: function that is with the parameters for reading data
        """

        self.path = None
        self.window = None
        self.has_header = BooleanVar(self.window)
        self.has_header.set(True) # Default

        self.callback = callback

        self.set_dataset = set_dataset
        self.delimiter = None

        self.gui = gui




    def init(self):
        """Initialize the view
        """
        self.window = Tk()
        self.path = filedialog.askopenfilename()

        self.window.title("Data input")

        lbl = ttk.Label(master=self.window,text = "Chosen file:\n"+self.path)
        lbl.grid(row=0,column=0)
        lbl.pack()

        options = ttk.Frame(master=self.window)

        ttk.Label(options, text='Delimiter:').grid(row=0,column=0)
        self.delimiter = ttk.Entry(options,width=2)
        self.delimiter.grid(row=0, column=1)
        self.delimiter.insert(0,";")

        Radiobutton(options
                        ,text='Header'
                        ,variable=self.has_header
                        ,value=True
                    ).grid(row=1,column=0)


        Radiobutton(options
                        ,text='No header'
                        ,variable=self.has_header
                        ,value=False
                    ).grid(row=1,column=1)


        # Load


        load_btn = ttk.Button(options ,text='Load dataset', command = self.load_data)
        load_btn.grid(row=2,column=0)

        # Pack
        options.pack()
        self.window.mainloop()


    def load_data(self):

        path = self.path
        delimiter = self.delimiter.get()
        has_header = self.has_header.get()

        self.read_data(path,delimiter,has_header)
        self.window.destroy()

    def read_data(self,path,delimiter,has_header,row_limit=None ):
        """Reads a dataset

        Args:
            row_limit: The number of rows to read from the data. All are read if None (default)
        """
        try:
            data = Dataset(FileAccess().read_csv(path, delimiter, '"', row_limit))
        except Exception as err:
            self.gui.show_warning(str(err))
            return

        data.create(has_header=has_header)

        self.set_dataset(data)

        filename_match = re.search('[a-z_]+\..+',path)

        self.callback({
                'fullpath': path,
                'filename': filename_match.group(),
                'delimiter': delimiter,
                'row_limit': row_limit,
                'has_header': has_header
            })
