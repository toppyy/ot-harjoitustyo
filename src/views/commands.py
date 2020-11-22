from tkinter import ttk, constants


class Commands:
    def __init__(self, root,stat_analyzer,display_analysis):
        self.root = root
        self.frame = None
        self.initialize()
        self.stat_analyzer = stat_analyzer
        self.display_analysis = display_analysis

    def initialize(self):
        
        self.frame = ttk.Frame(master=self.root,width=768, height=576)
        button = ttk.Button(master=self.frame, text="Summary", command=lambda: self.analyze("Summary"))
        button.grid(row=1, column=0)

    def analyze(self,which):

        print("Doing {}".format(which))

        self.display_analysis( self.stat_analyzer.summary("tyovoima") ) 

    def destroy(self):
        self.frame.destroy()
    
    def pack(self):
        self.frame.pack()