from tkinter import ttk, Tk, filedialog, Radiobutton, BooleanVar, messagebox
from file_access import FileAccess
from dataset import Dataset

class DataInput:

    def __init__(self, set_dataset, gui):

        self.path = filedialog.askopenfilename()
        self.window = Tk()
        self.has_header = BooleanVar(self.window)
        self.has_header.set(True) # Default

        self.set_dataset = set_dataset
        self.delimiter = None

        self.gui = gui

        self.init()


    def init(self):


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

        load_btn = ttk.Button(options ,text='Load dataset', command = self.read_data)
        load_btn.grid(row=2,column=0)

        # Pack
        options.pack()
        self.window.mainloop()


    def read_data(self,row_limit=None ):

        path = self.path
        delimiter = self.delimiter.get()
        has_header = self.has_header.get()


        data = Dataset(FileAccess().read_csv(path, delimiter, '"', row_limit))
        data.create(has_header=has_header, gui=self.gui)

        self.set_dataset(data)

        self.window.destroy()
